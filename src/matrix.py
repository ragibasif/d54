class Matrix:
    """Matrices from linear algebra"""
    def __init__(self,grid):
        self.matrix =[row.copy() for row in grid]
    @staticmethod
    def add(A,B):
        ar,ac,br,bc = len(A),len(A[0]),len(B),len(B[0])
        if not ar == br and ac == bc: return []
        C = [row.copy() for row in A]
        for row in range(ar):
            for col in range(ac):
                C[row][col] += B[row][col]
        return C
    @staticmethod
    def sub(A,B):
        ar,ac,br,bc = len(A),len(A[0]),len(B),len(B[0])
        if not ar == br and ac == bc: return []
        C = [row.copy() for row in A]
        for row in range(ar):
            for col in range(ac):
                C[row][col] -= B[row][col]
        return C
    @staticmethod
    def mul(A,B):
        # time: O(N*N*N)
        ar,ac,br,bc = len(A),len(A[0]),len(B),len(B[0])
        if not ar == bc and ac == br: return []
        cr = ar
        cc = bc
        C = [[0 for _ in range(cc)]for _ in range(cr)]
        def dot(row,col):
            # time: O(N)
            res = 0
            n = ac
            for i in range(n):
                res += A[row][i] * B[i][col]
            return res
        for row in range(cr): # time: O(N)
            for col in range(cc): # time: O(N)
                C[row][col] = dot(row,col) # time: O(N)
        return C

class Directions:
    """
    4-dir adjacent: the + shape  → (±1,0), (0,±1) -> one of dr or dc is 0
    4-dir diagonal: the x shape  → (±1,±1)        -> both dr and dc are nonzero
    8-dir:          the 3x3 grid → all combos of {-1,0,1} × {-1,0,1} except (0,0)

    Knight: L = 2+1 squares → all combos of {±1,±2} × {±2,±1}  (|dr|+|dc|==3, dr≠dc)
    King:   8-dir, 1 step
    Queen:  8-dir, infinite steps (while in bounds)
    Rook:   4-dir adjacent, infinite steps
    Bishop: 4-dir diagonal, infinite steps
    """
    def __init__(self):
        pass

    @staticmethod
    def in_bounds(r,c,rows,cols):
        return 0 <= r and r < rows and 0 <= c and c < cols

    @staticmethod
    def adjacent(): return [(-1,0),(1,0),(0,-1),(0,1)]

    @staticmethod
    def diagonal(): return [(-1,-1),(-1,1),(1,-1),(1,1)]

    @staticmethod
    def all():
        """
        [(-1,-1),(-1,0),(-1,1),
        ( 0,-1),        (0,1),
        ( 1,-1),( 1,0),( 1,1)]
        """
        return [(dr,dc) for dr in range(-1,2) for dc in range(-1,2) if (dr,dc) != (0,0)]

    @staticmethod
    def knight():
        """
        [(-2,-1),(-2,1),(-1,-2),(-1,2),
         ( 1,-2),( 1,2),( 2,-1),( 2,1)]
        """
        return [(dr, dc) for dr in range(-2, 3) for dc in range(-2, 3) if abs(dr) + abs(dc) == 3 and abs(dr) != abs(dc)]

    @staticmethod
    def king():
        return Directions.all()

    @staticmethod
    def queen():
        return Directions.all()

    @staticmethod
    def bishop():
        return Directions.diagonal()

    @staticmethod
    def rook():
        return Directions.adjacent()
