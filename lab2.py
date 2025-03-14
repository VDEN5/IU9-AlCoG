import glfw
from OpenGL.GL import *
from math import cos, sin

a = 0.0
b = 0.0
fill = True
cube_x = 0.0  # Новая переменная для перемещения куба по оси X
cube_y = 0.0  # Новая переменная для перемещения куба по оси Y


def main():
    if not glfw.init():
        return
    window = glfw.create_window(700, 700, "CUBE", None, None)
    if not window:
        glfw.terminate()
        return
    glfw.make_context_current(window)
    glfw.set_key_callback(window, key_callback)

    glEnable(GL_DEPTH_TEST)
    glDepthFunc(GL_LESS)

    while not glfw.window_should_close(window):
        display(window)
    glfw.destroy_window(window)
    glfw.terminate()


def display(window):
    glLoadIdentity()
    glClear(GL_COLOR_BUFFER_BIT)
    glClear(GL_DEPTH_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)

    # смещение
    glMultMatrixf([1, 0, 0, 0,
                   0, 1, 0, 0,
                   0, 0, 1, 0,
                   0.75, 0.75, 0, 1])

    t = -0.4
    p = 0.463648

    def Proj():  # фронтальная диметрия
        glMultMatrixf([
            cos(p), 0, sin(p), 0,
            0, cos(p), -cos(p) * sin(t), 0,
                       sin(p) * cos(t), -sin(t), -cos(t) * cos(p), 0,
            0, 0, 0, 1,
        ])

    Proj()

    def cube(x):
        x = x / 2
        glBegin(GL_QUADS)
        glColor3f(1.0, 0.0, 1.0)
        glVertex3f(-x + cube_x, -x + cube_y, -x)
        glVertex3f(-x + cube_x, x + cube_y, -x)
        glVertex3f(-x + cube_x, x + cube_y, x)
        glVertex3f(-x + cube_x, -x + cube_y, x)
        glColor3f(1.0, 0.5, 0.5)
        glVertex3f(x + cube_x, -x + cube_y, -x)
        glVertex3f(x + cube_x, -x + cube_y, x)
        glVertex3f(x + cube_x, x + cube_y, x)
        glVertex3f(x + cube_x, x + cube_y, -x)
        glColor3f(0.5, 1.0, 0.0)
        glVertex3f(-x + cube_x, -x + cube_y, -x)
        glVertex3f(-x + cube_x, -x + cube_y, x)
        glVertex3f(x + cube_x, -x + cube_y, x)
        glVertex3f(x + cube_x, -x + cube_y, -x)
        glColor3f(1.0, 1.0, 0.0)
        glVertex3f(-x + cube_x, x + cube_y, -x)
        glVertex3f(-x + cube_x, x + cube_y, x)
        glVertex3f(x + cube_x, x + cube_y, x)
        glVertex3f(x + cube_x, x + cube_y, -x)
        glColor3f(0.0, 1.0, 1.0)
        glVertex3f(-x + cube_x, -x + cube_y, -x)
        glVertex3f(x + cube_x, -x + cube_y, -x)
        glVertex3f(x + cube_x, x + cube_y, -x)
        glVertex3f(-x + cube_x, x + cube_y, -x)
        glColor3f(1.0, 0.5, 0.0)
        glVertex3f(-x + cube_x, -x + cube_y, x)
        glVertex3f(x + cube_x, -x + cube_y, x)
        glVertex3f(x + cube_x, x + cube_y, x)
        glVertex3f(-x + cube_x, x + cube_y, x)
        glEnd()

    cube(0.25)

    glLoadIdentity()

    global a
    global b
    t = -0.4 + a
    p = 0.463648 + b

    Proj()

    # Рисуем более крупный куб с учетом его положения
    cube(0.8)

    glfw.swap_buffers(window)
    glfw.poll_events()


def key_callback(window, key, scancode, action, mods):
    global a
    global b
    global cube_x  # Переменная для перемещения по оси X
    global cube_y  # Переменная для перемещения по оси Y

    if action == glfw.PRESS or action == glfw.REPEAT:
        if key == glfw.KEY_RIGHT:
            b += 0.05
        elif key == glfw.KEY_LEFT:
            b -= 0.05
        elif key == glfw.KEY_UP:
            a += 0.05
        elif key == glfw.KEY_DOWN:
            a -= 0.05

        # Перемещение по осям X и Y
        elif key == glfw.KEY_D:  # Вправо
            cube_x += 0.05
        elif key == glfw.KEY_A:  # Влево
            cube_x -= 0.05
        elif key == glfw.KEY_W:  # Вверх
            cube_y += 0.05
        elif key == glfw.KEY_S:  # Вниз
            cube_y -= 0.05

        elif key == glfw.KEY_F:
            global fill
            fill = not fill
            if fill:
                glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)
            else:
                glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
if __name__ == "__main__":
    main()
