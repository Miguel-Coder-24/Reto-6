import math

class Point:
    def __init__(self, x=0, y=0):
        # EXCEPCIÓN: Validamos que x e y sean numéricos
        if not isinstance(x, (int, float)) or not isinstance(y, (int, float)):
            raise TypeError("x e y deben ser numéricos.")
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def set_x(self, x):
        if isinstance(x, (int, float)):
            self._x = x
        else:
            raise TypeError("La coordenada x debe ser numérica.")  # EXCEPCIÓN

    def get_y(self):
        return self._y

    def set_y(self, y):
        if isinstance(y, (int, float)):
            self._y = y
        else:
            raise TypeError("La coordenada y debe ser numérica.")  # EXCEPCIÓN

    def __repr__(self):
        return f"Point({self._x}, {self._y})"

class Line:
    def __init__(self, start=None, end=None):
        if start is None:
            start = Point()
        if end is None:
            end = Point()

        if not isinstance(start, Point) or not isinstance(end, Point):
            raise TypeError("start y end deben ser objetos Point.")  # EXCEPCIÓN

        self._start = start
        self._end = end
        self._length = self.compute_length()
        self._slope = self.compute_slope()

    def get_start(self):
        return self._start

    def set_start(self, start):
        if isinstance(start, Point):
            self._start = start
            self._length = self.compute_length()
            self._slope = self.compute_slope()
        else:
            raise TypeError("El punto de inicio debe ser un objeto Point.")  # EXCEPCIÓN

    def get_end(self):
        return self._end

    def set_end(self, end):
        if isinstance(end, Point):
            self._end = end
            self._length = self.compute_length()
            self._slope = self.compute_slope()
        else:
            raise TypeError("El punto final debe ser un objeto Point.")  # EXCEPCIÓN

    def get_length(self):
        return self._length

    def get_slope(self):
        return self._slope

    def compute_length(self):
        dx = self._end.get_x() - self._start.get_x()
        dy = self._end.get_y() - self._start.get_y()
        return math.sqrt(dx**2 + dy**2)

    def compute_slope(self):
        dx = self._end.get_x() - self._start.get_x()
        dy = self._end.get_y() - self._start.get_y()
        if dx == 0:
            return 90.0 if dy > 0 else -90.0
        else:
            slope_rad = math.atan2(dy, dx)
            return math.degrees(slope_rad)

    def __repr__(self):
        return f"Line(Start={self._start}, End={self._end})"

class Shape:
    def __init__(self, vertices=None, edges=None, inner_angles=None, is_regular=False):
        if vertices is not None and not all(isinstance(v, Point) for v in vertices):
            raise TypeError("Todos los vértices deben ser objetos Point.")  # EXCEPCIÓN
        if edges is not None and not all(isinstance(e, Line) for e in edges):
            raise TypeError("Todas las aristas deben ser objetos Line.")  # EXCEPCIÓN
        if inner_angles is not None and not all(isinstance(a, (int, float)) for a in inner_angles):
            raise TypeError("inner_angles debe ser una lista de números.")  # EXCEPCIÓN
        if not isinstance(is_regular, bool):
            raise TypeError("is_regular debe ser un valor booleano.")  # EXCEPCIÓN

        self._vertices = vertices if vertices is not None else []
        self._edges = edges if edges is not None else []
        self._inner_angles = inner_angles if inner_angles is not None else []
        self._is_regular = is_regular

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        if isinstance(vertices, list) and all(isinstance(v, Point) for v in vertices):
            self._vertices = vertices
        else:
            raise TypeError("vertices debe ser una lista de objetos Point.")  # EXCEPCIÓN

    def get_edges(self):
        return self._edges

    def set_edges(self, edges):
        if isinstance(edges, list) and all(isinstance(e, Line) for e in edges):
            self._edges = edges
        else:
            raise TypeError("edges debe ser una lista de objetos Line.")  # EXCEPCIÓN

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, angles):
        if isinstance(angles, list) and all(isinstance(a, (int, float)) for a in angles):
            self._inner_angles = angles
        else:
            raise TypeError("inner_angles debe ser una lista de números.")  # EXCEPCIÓN

    def get_is_regular(self):
        return self._is_regular

    def set_is_regular(self, is_regular):
        if isinstance(is_regular, bool):
            self._is_regular = is_regular
        else:
            raise TypeError("is_regular debe ser booleano.")  # EXCEPCIÓN

    def compute_area(self):
        print("compute_area no implementado para Shape base.")
        return None

    def compute_perimeter(self):
        print("compute_perimeter no implementado para Shape base.")
        return None

    def compute_inner_angles(self):
        print("compute_inner_angles no implementado para Shape base.")
        return None

class Triangle(Shape):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices=vertices, edges=edges)
        if vertices and len(vertices) == 3:
            self._edges = [
                Line(vertices[0], vertices[1]),
                Line(vertices[1], vertices[2]),
                Line(vertices[2], vertices[0])
            ]
        elif edges and len(edges) == 3:
            self._vertices = [
                edges[0].get_start(),
                edges[0].get_end(),
                edges[1].get_end()
            ]
        else:
            raise ValueError("Un triángulo debe tener 3 vértices o 3 aristas.")  # EXCEPCIÓN

    def compute_area(self):
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        s = (a + b + c) / 2
        try:
            return math.sqrt(s * (s - a) * (s - b) * (s - c))  # puede fallar si no es un triángulo válido
        except ValueError:
            raise ValueError("No es un triángulo válido para cálculo de área.")  # EXCEPCIÓN

    def compute_perimeter(self):
        return sum(edge.get_length() for edge in self._edges)

    def compute_inner_angles(self):
        a = self._edges[0].get_length()
        b = self._edges[1].get_length()
        c = self._edges[2].get_length()
        try:
            angle_A = math.degrees(math.acos((b**2 + c**2 - a**2) / (2*b*c)))
            angle_B = math.degrees(math.acos((a**2 + c**2 - b**2) / (2*a*c)))
            angle_C = 180 - angle_A - angle_B
            self._inner_angles = [angle_A, angle_B, angle_C]
            return self._inner_angles
        except ValueError:
            raise ValueError("Ángulos no válidos para triángulo.")  # EXCEPCIÓN

# Subclases de Triángulo solo imprimen advertencias (no detienen ejecución)
class Isosceles(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(False)
        lengths = [edge.get_length() for edge in self._edges]
        tolerance = 1e-6
        if not (
            abs(lengths[0] - lengths[1]) < tolerance or
            abs(lengths[1] - lengths[2]) < tolerance or
            abs(lengths[2] - lengths[0]) < tolerance
        ):
            print("Advertencia: Este triángulo no cumple la condición de isósceles.")

class Equilateral(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(True)
        lengths = [edge.get_length() for edge in self._edges]
        tolerance = 1e-6
        if not (abs(lengths[0] - lengths[1]) < tolerance and abs(lengths[1] - lengths[2]) < tolerance):
            print("Advertencia: Este triángulo no es equilátero.")

class Scalene(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(False)
        lengths = [edge.get_length() for edge in self._edges]
        tolerance = 1e-6
        if (abs(lengths[0] - lengths[1]) < tolerance or
            abs(lengths[1] - lengths[2]) < tolerance or
            abs(lengths[2] - lengths[0]) < tolerance):
            print("Advertencia: Este triángulo no es escaleno (tiene lados iguales).")

class TriRectangle(Triangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(False)
        self.compute_inner_angles()
        if 90 not in [round(angle) for angle in self._inner_angles]:
            print("Advertencia: Este triángulo no es rectángulo (no tiene un ángulo de 90 grados).")

class Rectangle(Shape):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices=vertices, edges=edges)
        self.set_is_regular(True)

        if vertices and len(vertices) == 4:
            self._edges = [
                Line(vertices[0], vertices[1]),
                Line(vertices[1], vertices[2]),
                Line(vertices[2], vertices[3]),
                Line(vertices[3], vertices[0])
            ]
        elif edges and len(edges) == 4:
            self._vertices = [
                edges[0].get_start(),
                edges[0].get_end(),
                edges[1].get_end(),
                edges[2].get_end()
            ]
        else:
            raise ValueError("Un rectángulo debe tener 4 vértices o 4 aristas.")  # EXCEPCIÓN

        self._width = self._edges[0].get_length()
        self._height = self._edges[1].get_length()

    def compute_area(self):
        return self._width * self._height

    def compute_perimeter(self):
        return 2 * (self._width + self._height)

    def compute_inner_angles(self):
        self._inner_angles = [90, 90, 90, 90]
        return self._inner_angles

class Square(Rectangle):
    def __init__(self, vertices=None, edges=None):
        super().__init__(vertices, edges)
        self.set_is_regular(True)
        sides = [edge.get_length() for edge in self._edges]
        tolerance = 1e-6
        if not all(abs(sides[0] - s) < tolerance for s in sides[1:]):
            print("Advertencia: Este cuadrado no tiene todos los lados iguales.")
