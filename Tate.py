class E:
    def __init__(self, a1, a2, a3, a4, a6):
        self._a1 = a1
        self._a2 = a2
        self._a3 = a3
        self._a4 = a4
        self._a6 = a6

    def __repr__(self):
        s = "y^2"
        monomials_l = ["xy", "y"]
        monomials_r = ["x^2", "x", ""]
        s_l = "y^2"
        s_r = "x^3"
        for c, m in zip([self.a1, self.a3], monomials_l):
            if c < 0:
                a = -c if c != -1 else ""
                s_l += f" - {a}x{m}"
            elif c > 0:
                a = c if c != 1 else ""
                s_l += f" + {a}x{m}"
        for c, m in zip([self.a2, self.a4, self.a6], monomials_r):
            if c < 0:
                a = -c if c != -1 else ""
                s_r += f" - {a}{m}"
            elif c > 0:
                a = c if c != 1 else ""
                s_r += f" + {a}{m}"
        return s_l + " = " + s_r

    @property
    def a1(self):
        return self._a1

    @property
    def a2(self):
        return self._a2

    @property
    def a3(self):
        return self._a3

    @property
    def a4(self):
        return self._a4

    @property
    def a6(self):
        return self._a6

    @property
    def b2(self):
        return self.a1**2 + 4 * self.a2

    @property
    def b4(self):
        return 2 * self.a4 + self.a1 * self.a3

    @property
    def b6(self):
        return self.a3**2 + 4 * self.a6

    @property
    def b8(self):
        return (
            self.a1**2 * self.a6
            + 4 * self.a2 * self.a6
            - self.a1 * self.a3 * self.a4
            + self.a2 * self.a3**2
            - self.a4**2
        )

    @property
    def c4(self):
        return self.b2**2 - 24 * self.b4

    @property
    def c6(self):
        return -self.b2**3 + 36 * self.b2 * self.b4 - 216 * self.b6

    @property
    def delta(self):
        return (
            -self.b2**2 * self.b8
            - 8 * self.b4**3
            - 27 * self.b6**2
            + 9 * self.b2 * self.b4 * self.b6
        )

    @property
    def j(self):
        return 1728 * (self.b2**3) / self.delta
