#include <GL/glut.h>
#include <cmath>
#include <fstream>
#include <iostream>
#include <sstream>
#include <stdlib.h>
#include <vector>
#include <vecmath.h>
using namespace std;

/* Scratchpad
//DEBUG
// for determining types:
    #include <typeinfo>
    cout << typeid(variablename).name() << '\n';

*/

// Globals
bool rotating = false;
unsigned angle = 0;
int timerDelay = 40;

// Global display list
GLuint displayIndex;

// This is the list of points (3D vectors)
vector<Vector3f> vecv;

// This is the list of normals (also 3D vectors)
vector<Vector3f> vecn;

// This is the list of faces (indices into vecv and vecn)
vector<vector<unsigned> > vecf;

// Light offsets
float light_h_offset = 1.0f;
float light_v_offset = 1.0f;

// Color globals
GLfloat targetColors[4] = {0.5f, 0.5f, 0.5f, 1.0f};
GLfloat currentColors[4] = {0.5f, 0.5f, 0.5f, 1.0f};

// These are convenience functions which allow us to call OpenGL 
// methods on Vec3d objects
inline void glVertex(const Vector3f &a) 
{ glVertex3fv(a); }

inline void glNormal(const Vector3f &a) 
{ glNormal3fv(a); }

GLfloat getRandColor()
{
    // Get a random number, set the range between 0-99, convert to value between 0 and 1
    return rand() % 1000 / 1000.0;
}

void swapColors()
{
    // Our colors consist of 3 random values, and 1 constant for RGBA (red, green, blue, alpha) reflectance of the material
    // Reference: http://msdn.microsoft.com/en-us/library/windows/desktop/dd373945(v=vs.85).aspx
    //cout << "swapping colors" << endl;
    targetColors[0] = getRandColor();
    targetColors[1] = getRandColor();
    targetColors[2] = getRandColor();

    //for (int i = 0; i < 3; i++)
    //{
    //    cout << "Target color " << i << " " << targetColors[i] << endl;
    //    cout << "Current color " << i << " " << currentColors[i] << endl;
    //}
}

bool colorOutOfDate()
{
    return (currentColors[0] != targetColors[0] ||
            currentColors[1] != targetColors[1] ||
            currentColors[2] != targetColors[2]);
}

void timerCallback(int val)
{
    if (colorOutOfDate())
    {
        for (int i = 0; i < 3; i++)
        {
            GLfloat diff = targetColors[i] - currentColors[i];
            if (diff == 0)
            {
                continue;
            }
            else if (diff < 0.01)
            {
                currentColors[i] = targetColors[i];
            }
            else if (diff < 0)
            {
                currentColors[i] -= 0.01;
            }
            else // (diff > 0)
            {
                currentColors[i] += 0.01;
            }
        }
    }
    if (rotating)
    {
        angle += 1;
    }
    glutPostRedisplay();
    // Re-enable timer if rotation bool hasn't been disabled
    if (rotating or colorOutOfDate())
    {
        // time in usecs, callback, value for callback
        glutTimerFunc(timerDelay, timerCallback, 0);
    }
}

// This function is called whenever a "Normal" key press is received.
void keyboardFunc( unsigned char key, int x, int y )
{
    switch ( key )
    {
    case 27: // Escape key
        exit(0);
        break;
    case 'c':
        // this will refresh the screen so that the user sees the color change
        swapColors();
        // update colors
        glutTimerFunc(timerDelay, timerCallback, 0);
        break;
    case 'r':
        rotating = !rotating;
        glutTimerFunc(timerDelay, timerCallback, 0);
        break;
    default:
        cout << "Unhandled key press " << key << "." << endl;        
    }
    /*
    //DEBUG
    //cout << "RGBA: " << randColors[0] << " : " << randColors[1] << " : " << randColors[2] << " : " << randColors[3] << endl;
    */
    // redraw the scene
    glutPostRedisplay();
}

// This function is called whenever a "Special" key press is received.
// Right now, it's handling the arrow keys.
void specialFunc( int key, int x, int y )
{
    switch ( key )
    {
    case GLUT_KEY_UP:
        // add code to change light position
        light_v_offset += 0.5f;
        break;
    case GLUT_KEY_DOWN:
        // add code to change light position
        light_v_offset -= 0.5f;
        break;
    case GLUT_KEY_LEFT:
        // add code to change light position
        light_h_offset -= 0.5f;
        break;
    case GLUT_KEY_RIGHT:
        // add code to change light position
        light_h_offset += 0.5f;
        break;
    }

    // this will refresh the screen so that the user sees the light position
    /*
    //DEBUG
    cout << "Light vertical offset: " << light_v_offset << endl;
    cout << "Light horizontal offset: " << light_h_offset << endl;
    */
    glutPostRedisplay();
}

// This function is responsible for displaying the object.
void drawScene()
{
    int i;

    // Clear the rendering window
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);

    // Rotate the image
    glMatrixMode( GL_MODELVIEW );  // Current matrix affects objects positions
    glLoadIdentity();              // Initialize to the identity

    // Rotates on z-axis
    glRotatef(angle, 0, 0, 1);

    // Position the camera at [0,0,5], looking at [0,0,0],
    // with [0,1,0] as the up direction.
    gluLookAt(0.0, 0.0, 5.0,
              0.0, 0.0, 0.0,
              0.0, 1.0, 0.0);
    
	// Here we use the first color entry as the diffuse color
    glMaterialfv(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE, currentColors);

	// Define specular color and shininess
    GLfloat specColor[] = {1.0, 1.0, 1.0, 1.0};
    GLfloat shininess[] = {100.0};

	// Note that the specular color and shininess can stay constant
    glMaterialfv(GL_FRONT_AND_BACK, GL_SPECULAR, specColor);
    glMaterialfv(GL_FRONT_AND_BACK, GL_SHININESS, shininess);
  
    // Set light properties

    // Light color (RGBA)
    GLfloat Lt0diff[] = {1.0,1.0,1.0,1.0};
    // Light position
	GLfloat Lt0pos[] = {light_h_offset, light_v_offset, 5.0f, 1.0f};

    glLightfv(GL_LIGHT0, GL_DIFFUSE, Lt0diff);
    glLightfv(GL_LIGHT0, GL_POSITION, Lt0pos);

	// This GLUT method draws a teapot.  You should replace
	// it with code which draws the object you loaded.
    if (vecv.size() == 0)
    {
	   glutSolidTeapot(1.0);
    }
    else
    {
        glCallList(displayIndex);
    }
    
    // Dump the image to the screen.
    glutSwapBuffers();
}

// Initialize OpenGL's rendering modes
void initRendering()
{
    glEnable(GL_DEPTH_TEST);   // Depth testing must be turned on
    glEnable(GL_LIGHTING);     // Enable lighting calculations
    glEnable(GL_LIGHT0);       // Turn on light #0.
}

// Called when the window is resized
// w, h - width and height of the window in pixels.
void reshapeFunc(int w, int h)
{
    // Always use the largest square viewport possible
    if (w > h) {
        glViewport((w - h) / 2, 0, h, h);
    } else {
        glViewport(0, (h - w) / 2, w, w);
    }

    // Set up a perspective view, with square aspect ratio
    glMatrixMode(GL_PROJECTION);
    glLoadIdentity();
    // 50 degree fov, uniform aspect ratio, near = 1, far = 100
    gluPerspective(50.0, 1.0, 1.0, 100.0);
}

void loadInput(char* infileName)
{
	// load the OBJ file here, to globals... which
    //  you know, feels pretty gross.
    // 1. create char buffer
    // 2. read cin line by line
    // 3. populate vertices, normals, and faces from cin
    // 4. exit when cin is 0

    ifstream infile(infileName);
    string buffer;

    // Ingest cin until we get our EOF notification.
    // cin.getline returns 0 once EOF is hit.
    int faces = 0;
    while (getline(infile, buffer))
    {
        stringstream ss(buffer);
        string primitive;
        ss >> primitive;
        if (primitive == "v")
        {
            // we are expecting points in the ascii format of
            // a leading 'v' followed by three numeric values, 
            // for example: v 1.2 3.1 1.0
            Vector3f v;
            // apparently this does an implicit typecast from string
            // to float, so that's pretty convenient
            ss >> v[0] >> v[1] >> v[2];
            vecv.push_back(v);
        }
        else if (primitive == "vn")
        {
            // we are expecting normals in the ascii format of
            // a leading 'vn' followed by three numeric values, 
            // for example: v 1.2 3.1 1.0
            Vector3f v;
            ss >> v[0] >> v[1] >> v[2];
            vecn.push_back(v);
        }
        else if (primitive == "f")
        {
            // we are expecting faces in the ascii format of
            // a leading 'f' followed by three groups of 3 values, 
            // for example: f 1/2/3 4/5/6 7/8/9
            string line;
            // parse line by line
            while(getline(ss, line))
            {
                vector<unsigned> v;
                stringstream linestream(line);
                string spacedGroup;
                // Split each line on spaces, and below we will split on slashes
                while(getline(linestream, spacedGroup, ' '))
                {
                    // Empty strings show up when splitting on spaces because: reasons
                    if (spacedGroup == "")
                    {
                        continue;
                    }
                    stringstream spacedGroupStream(spacedGroup);
                    string numval;
                    // Now split on slashes, and we have individual strings to cast to unsigned
                    while(getline(spacedGroupStream, numval, '/'))
                    {
                        // cast string to unsigned, this should be stoi() actually
                        v.push_back(unsigned(atoi(numval.c_str())));
                    }
                }
                vecf.push_back(v);
            }
        }
    }
    if (vecf.size() > 0)
    {
        // Load the geometry into a display list
        // compile the display list, store a triangle in it
        // IMPORTANT: don't do anything GL related until fully initialized...
        displayIndex = glGenLists(1);
        glNewList(displayIndex, GL_COMPILE_AND_EXECUTE);
        //  1. iterate over faces
        //  2. create normals, then vertices
        glBegin(GL_TRIANGLES);
        for (size_t k = 0; k < vecf.size(); k++)
        {
            // setup references to face indices
            int a = vecf[k][0] - 1;
            int b = vecf[k][1] - 1;
            int c = vecf[k][2] - 1;
            int d = vecf[k][3] - 1;
            int e = vecf[k][4] - 1;
            int f = vecf[k][5] - 1;
            int g = vecf[k][6] - 1;
            int h = vecf[k][7] - 1;
            int i = vecf[k][8] - 1;

            /*
            //DEBUG
            cout << "a: " << a << endl;
            cout << "b: " << b << endl;
            cout << "c: " << c << endl;
            cout << "d: " << d << endl;
            cout << "e: " << e << endl;
            cout << "f: " << f << endl;
            cout << "g: " << g << endl;
            cout << "h: " << h << endl;
            cout << "i: " << i << endl;
            */

            glNormal3d(vecn[c][0], vecn[c][1], vecn[c][2]);
            glVertex3d(vecv[a][0], vecv[a][1], vecv[a][2]);
            glNormal3d(vecn[f][0], vecn[f][1], vecn[f][2]);
            glVertex3d(vecv[d][0], vecv[d][1], vecv[d][2]);
            glNormal3d(vecn[i][0], vecn[i][1], vecn[i][2]);
            glVertex3d(vecv[g][0], vecv[g][1], vecv[g][2]);
        }
        glEnd();
        glEndList();    
    }
    /*
    //DEBUG
    // report some debug information to sanity check inputs
    cout << "vertex count: " << vecv.size() << endl;
    cout << "normal count: " << vecn.size() << endl;
    cout << "face count: " << vecf.size() << endl;
    cout << "Geometry is parsed, loading now..." << endl;
    */
}

// Main routine.
// Set up OpenGL, define the callbacks and start the main loop
int main( int argc, char** argv )
{
    // IMPORTANT: don't do anything GL related until fully initialized...
    //  there will be no errors, but there will be tears.
    glutInit(&argc,argv);

    // We're going to animate it, so double buffer 
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH );

    // Initial parameters for window position and size
    glutInitWindowPosition( 60, 60 );
    glutInitWindowSize( 360, 360 );
    glutCreateWindow("Assignment 0");

    // Initialize OpenGL parameters.
    initRendering();

    // Set up callback functions for key presses
    glutKeyboardFunc(keyboardFunc); // Handles "normal" ascii symbols
    glutSpecialFunc(specialFunc);   // Handles "special" keyboard keys

     // Set up the callback function for resizing windows
    glutReshapeFunc( reshapeFunc );

    // Call this whenever window needs redrawing
    glutDisplayFunc( drawScene );

    // pass filename to load, if apropos
    if (argc > 1)
    {
        loadInput(argv[1]);
    }

    // Start the main loop.  glutMainLoop never returns.
    glutMainLoop( );

    return 0;	// This line is never reached.
}
