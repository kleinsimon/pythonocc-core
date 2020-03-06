from typing import NewType, Optional, Tuple

from OCC.Core.BRepAdaptor import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TopoDS import *
from OCC.Core.Geom import *
from OCC.Core.gp import *
from OCC.Core.GeomAbs import *
from OCC.Core.TColStd import *
from OCC.Core.GeomAdaptor import *
from OCC.Core.Geom2dAdaptor import *
from OCC.Core.Adaptor2d import *


class BRepAdaptor_CompCurve(Adaptor3d_Curve):
	def __init__(self) -> None: ...
	def __init__(self, W: TopoDS_Wire, KnotByCurvilinearAbcissa: Optional[bool]) -> None: ...
	def __init__(self, W: TopoDS_Wire, KnotByCurvilinearAbcissa: bool, First: float, Last: float, Tol: float) -> None: ...
	def BSpline(self) -> Geom_BSplineCurve: ...
	def Bezier(self) -> Geom_BezierCurve: ...
	def Circle(self) -> gp_Circ: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
	def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec: ...
	def Degree(self) -> int: ...
	def Edge(self, U: float, E: TopoDS_Edge) -> float: ...
	def Ellipse(self) -> gp_Elips: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr: ...
	def Initialize(self, W: TopoDS_Wire, KnotByCurvilinearAbcissa: bool) -> None: ...
	def Initialize(self, W: TopoDS_Wire, KnotByCurvilinearAbcissa: bool, First: float, Last: float, Tol: float) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def IsClosed(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def Parabola(self) -> gp_Parab: ...
	def Period(self) -> float: ...
	def Resolution(self, R3d: float) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
	def Value(self, U: float) -> gp_Pnt: ...
	def Wire(self) -> TopoDS_Wire: ...

class BRepAdaptor_Curve(Adaptor3d_Curve):
	def __init__(self) -> None: ...
	def __init__(self, E: TopoDS_Edge) -> None: ...
	def __init__(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def BSpline(self) -> Geom_BSplineCurve: ...
	def Bezier(self) -> Geom_BezierCurve: ...
	def Circle(self) -> gp_Circ: ...
	def Continuity(self) -> GeomAbs_Shape: ...
	def Curve(self) -> GeomAdaptor_Curve: ...
	def CurveOnSurface(self) -> Adaptor3d_CurveOnSurface: ...
	def D0(self, U: float, P: gp_Pnt) -> None: ...
	def D1(self, U: float, P: gp_Pnt, V: gp_Vec) -> None: ...
	def D2(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec) -> None: ...
	def D3(self, U: float, P: gp_Pnt, V1: gp_Vec, V2: gp_Vec, V3: gp_Vec) -> None: ...
	def DN(self, U: float, N: int) -> gp_Vec: ...
	def Degree(self) -> int: ...
	def Edge(self) -> TopoDS_Edge: ...
	def Ellipse(self) -> gp_Elips: ...
	def FirstParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_CurveType: ...
	def Hyperbola(self) -> gp_Hypr: ...
	def Initialize(self, E: TopoDS_Edge) -> None: ...
	def Initialize(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def Intervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def Is3DCurve(self) -> bool: ...
	def IsClosed(self) -> bool: ...
	def IsCurveOnSurface(self) -> bool: ...
	def IsPeriodic(self) -> bool: ...
	def IsRational(self) -> bool: ...
	def LastParameter(self) -> float: ...
	def Line(self) -> gp_Lin: ...
	def NbIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbKnots(self) -> int: ...
	def NbPoles(self) -> int: ...
	def OffsetCurve(self) -> Geom_OffsetCurve: ...
	def Parabola(self) -> gp_Parab: ...
	def Period(self) -> float: ...
	def Reset(self) -> None: ...
	def Resolution(self, R3d: float) -> float: ...
	def Tolerance(self) -> float: ...
	def Trim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HCurve: ...
	def Trsf(self) -> gp_Trsf: ...
	def Value(self, U: float) -> gp_Pnt: ...

class BRepAdaptor_Curve2d(Geom2dAdaptor_Curve):
	def __init__(self) -> None: ...
	def __init__(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def Edge(self) -> TopoDS_Edge: ...
	def Face(self) -> TopoDS_Face: ...
	def Initialize(self, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...

class BRepAdaptor_HCompCurve(Adaptor3d_HCurve):
	def __init__(self) -> None: ...
	def __init__(self, C: BRepAdaptor_CompCurve) -> None: ...
	def ChangeCurve(self) -> BRepAdaptor_CompCurve: ...
	def Curve(self) -> Adaptor3d_Curve: ...
	def GetCurve(self) -> Adaptor3d_Curve: ...
	def Set(self, C: BRepAdaptor_CompCurve) -> None: ...

class BRepAdaptor_HCurve(Adaptor3d_HCurve):
	def __init__(self) -> None: ...
	def __init__(self, C: BRepAdaptor_Curve) -> None: ...
	def ChangeCurve(self) -> BRepAdaptor_Curve: ...
	def Curve(self) -> Adaptor3d_Curve: ...
	def GetCurve(self) -> Adaptor3d_Curve: ...
	def Set(self, C: BRepAdaptor_Curve) -> None: ...

class BRepAdaptor_HCurve2d(Adaptor2d_HCurve2d):
	def __init__(self) -> None: ...
	def __init__(self, C: BRepAdaptor_Curve2d) -> None: ...
	def ChangeCurve2d(self) -> BRepAdaptor_Curve2d: ...
	def Curve2d(self) -> Adaptor2d_Curve2d: ...
	def Set(self, C: BRepAdaptor_Curve2d) -> None: ...

class BRepAdaptor_HSurface(Adaptor3d_HSurface):
	def __init__(self) -> None: ...
	def __init__(self, S: BRepAdaptor_Surface) -> None: ...
	def ChangeSurface(self) -> BRepAdaptor_Surface: ...
	def Set(self, S: BRepAdaptor_Surface) -> None: ...
	def Surface(self) -> Adaptor3d_Surface: ...

class BRepAdaptor_Surface(Adaptor3d_Surface):
	def __init__(self) -> None: ...
	def __init__(self, F: TopoDS_Face, R: Optional[bool]) -> None: ...
	def AxeOfRevolution(self) -> gp_Ax1: ...
	def BSpline(self) -> Geom_BSplineSurface: ...
	def BasisCurve(self) -> Adaptor3d_HCurve: ...
	def BasisSurface(self) -> Adaptor3d_HSurface: ...
	def Bezier(self) -> Geom_BezierSurface: ...
	def ChangeSurface(self) -> GeomAdaptor_Surface: ...
	def Cone(self) -> gp_Cone: ...
	def Cylinder(self) -> gp_Cylinder: ...
	def D0(self, U: float, V: float, P: gp_Pnt) -> None: ...
	def D1(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec) -> None: ...
	def D2(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec) -> None: ...
	def D3(self, U: float, V: float, P: gp_Pnt, D1U: gp_Vec, D1V: gp_Vec, D2U: gp_Vec, D2V: gp_Vec, D2UV: gp_Vec, D3U: gp_Vec, D3V: gp_Vec, D3UUV: gp_Vec, D3UVV: gp_Vec) -> None: ...
	def DN(self, U: float, V: float, Nu: int, Nv: int) -> gp_Vec: ...
	def Direction(self) -> gp_Dir: ...
	def Face(self) -> TopoDS_Face: ...
	def FirstUParameter(self) -> float: ...
	def FirstVParameter(self) -> float: ...
	def GetType(self) -> GeomAbs_SurfaceType: ...
	def Initialize(self, F: TopoDS_Face, Restriction: Optional[bool]) -> None: ...
	def IsUClosed(self) -> bool: ...
	def IsUPeriodic(self) -> bool: ...
	def IsURational(self) -> bool: ...
	def IsVClosed(self) -> bool: ...
	def IsVPeriodic(self) -> bool: ...
	def IsVRational(self) -> bool: ...
	def LastUParameter(self) -> float: ...
	def LastVParameter(self) -> float: ...
	def NbUIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbUKnots(self) -> int: ...
	def NbUPoles(self) -> int: ...
	def NbVIntervals(self, S: GeomAbs_Shape) -> int: ...
	def NbVKnots(self) -> int: ...
	def NbVPoles(self) -> int: ...
	def OffsetValue(self) -> float: ...
	def Plane(self) -> gp_Pln: ...
	def Sphere(self) -> gp_Sphere: ...
	def Surface(self) -> GeomAdaptor_Surface: ...
	def Tolerance(self) -> float: ...
	def Torus(self) -> gp_Torus: ...
	def Trsf(self) -> gp_Trsf: ...
	def UContinuity(self) -> GeomAbs_Shape: ...
	def UDegree(self) -> int: ...
	def UIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def UPeriod(self) -> float: ...
	def UResolution(self, R3d: float) -> float: ...
	def UTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
	def VContinuity(self) -> GeomAbs_Shape: ...
	def VDegree(self) -> int: ...
	def VIntervals(self, T: TColStd_Array1OfReal, S: GeomAbs_Shape) -> None: ...
	def VPeriod(self) -> float: ...
	def VResolution(self, R3d: float) -> float: ...
	def VTrim(self, First: float, Last: float, Tol: float) -> Adaptor3d_HSurface: ...
	def Value(self, U: float, V: float) -> gp_Pnt: ...
