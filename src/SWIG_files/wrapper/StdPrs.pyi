from typing import NewType, Optional, Tuple

from OCC.Core.StdPrs import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.Geom import *
from OCC.Core.Prs3d import *
from OCC.Core.Bnd import *
from OCC.Core.Graphic3d import *
from OCC.Core.gp import *
from OCC.Core.Adaptor3d import *
from OCC.Core.TColgp import *
from OCC.Core.TopoDS import *
from OCC.Core.HLRAlgo import *
from OCC.Core.BRepAdaptor import *
from OCC.Core.TColStd import *
from OCC.Core.Poly import *
from OCC.Core.TopLoc import *
from OCC.Core.BRep import *
from OCC.Core.GeomAbs import *
from OCC.Core.TopAbs import *
from OCC.Core.Adaptor2d import *


class StdPrs_Volume:
	StdPrs_Volume_Autodetection: int = ...
	StdPrs_Volume_Closed: int = ...
	StdPrs_Volume_Opened: int = ...

class StdPrs_BndBox(Prs3d_Root):
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theBndBox: Bnd_Box, theDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theBndBox: Bnd_OBB, theDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def FillSegments(self, theBox: Bnd_OBB) -> Graphic3d_ArrayOfSegments: ...
	@staticmethod
	def FillSegments(self, theBox: Bnd_Box) -> Graphic3d_ArrayOfSegments: ...
	@staticmethod
	def FillSegments(self, theSegments: Graphic3d_ArrayOfSegments, theBox: Bnd_OBB) -> None: ...
	@staticmethod
	def FillSegments(self, theSegments: Graphic3d_ArrayOfSegments, theBox: Bnd_Box) -> None: ...
	@staticmethod
	def fillSegments(self, theSegments: Graphic3d_ArrayOfSegments, theBox: gp_Pnt) -> None: ...

class StdPrs_Curve(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer, drawCurve: Optional[bool]) -> None: ...
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, U1: float, U2: float, aDrawer: Prs3d_Drawer, drawCurve: Optional[bool]) -> None: ...
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer, Points: TColgp_SequenceOfPnt, drawCurve: Optional[bool]) -> None: ...
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, U1: float, U2: float, Points: TColgp_SequenceOfPnt, aNbPoints: Optional[int], drawCurve: Optional[bool]) -> None: ...
	@staticmethod
	def Match(self, X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def Match(self, X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, aDeflection: float, aLimit: float, aNbPoints: int) -> bool: ...
	@staticmethod
	def Match(self, X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, U1: float, U2: float, aDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def Match(self, X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, U1: float, U2: float, aDeflection: float, aNbPoints: int) -> bool: ...

class StdPrs_HLRPolyShape(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aShape: TopoDS_Shape, aDrawer: Prs3d_Drawer, aProjector: Prs3d_Projector) -> None: ...

class StdPrs_HLRShape(Prs3d_Root):
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theProjector: Prs3d_Projector) -> None: ...

class StdPrs_HLRToolShape:
	def __init__(self, TheShape: TopoDS_Shape, TheProjector: HLRAlgo_Projector) -> None: ...
	def Hidden(self, TheEdge: BRepAdaptor_Curve) -> Tuple[float, float]: ...
	def InitHidden(self, EdgeNumber: int) -> None: ...
	def InitVisible(self, EdgeNumber: int) -> None: ...
	def MoreHidden(self) -> bool: ...
	def MoreVisible(self) -> bool: ...
	def NbEdges(self) -> int: ...
	def NextHidden(self) -> None: ...
	def NextVisible(self) -> None: ...
	def Visible(self, TheEdge: BRepAdaptor_Curve) -> Tuple[float, float]: ...

class StdPrs_Isolines(Prs3d_Root):
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theDeflection: float) -> None: ...
	@staticmethod
	def Add(self, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theDeflection: float, theUPolylines: Prs3d_NListOfSequenceOfPnt, theVPolylines: Prs3d_NListOfSequenceOfPnt) -> None: ...
	@staticmethod
	def AddOnSurface(self, thePresentation: Prs3d_Presentation, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theDeflection: float) -> None: ...
	@staticmethod
	def AddOnSurface(self, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theDeflection: float, theUPolylines: Prs3d_NListOfSequenceOfPnt, theVPolylines: Prs3d_NListOfSequenceOfPnt) -> None: ...
	@staticmethod
	def AddOnSurface(self, thePresentation: Prs3d_Presentation, theSurface: BRepAdaptor_HSurface, theDrawer: Prs3d_Drawer, theDeflection: float, theUIsoParams: TColStd_SequenceOfReal, theVIsoParams: TColStd_SequenceOfReal) -> None: ...
	@staticmethod
	def AddOnTriangulation(self, thePresentation: Prs3d_Presentation, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def AddOnTriangulation(self, theFace: TopoDS_Face, theDrawer: Prs3d_Drawer, theUPolylines: Prs3d_NListOfSequenceOfPnt, theVPolylines: Prs3d_NListOfSequenceOfPnt) -> None: ...
	@staticmethod
	def AddOnTriangulation(self, thePresentation: Prs3d_Presentation, theTriangulation: Poly_Triangulation, theSurface: Geom_Surface, theLocation: TopLoc_Location, theDrawer: Prs3d_Drawer, theUIsoParams: TColStd_SequenceOfReal, theVIsoParams: TColStd_SequenceOfReal) -> None: ...
	@staticmethod
	def UVIsoParameters(self, theFace: TopoDS_Face, theNbIsoU: int, theNbIsoV: int, theUVLimit: float, theUIsoParams: TColStd_SequenceOfReal, theVIsoParams: TColStd_SequenceOfReal) -> Tuple[float, float, float, float]: ...

class StdPrs_Plane(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aPlane: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def Match(self, X: float, Y: float, Z: float, aDistance: float, aPlane: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> bool: ...

class StdPrs_PoleCurve(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def Match(self, X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def Pick(self, X: float, Y: float, Z: float, aDistance: float, aCurve: Adaptor3d_Curve, aDrawer: Prs3d_Drawer) -> int: ...

class StdPrs_ShadedShape(Prs3d_Root):
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theVolume: Optional[StdPrs_Volume]) -> None: ...
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theHasTexels: bool, theUVOrigin: gp_Pnt2d, theUVRepeat: gp_Pnt2d, theUVScale: gp_Pnt2d, theVolume: Optional[StdPrs_Volume]) -> None: ...
	@staticmethod
	def AddWireframeForFacesWithoutTriangles(self, thePrs: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def AddWireframeForFreeElements(self, thePrs: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def ExploreSolids(self, theShape: TopoDS_Shape, theBuilder: BRep_Builder, theClosed: TopoDS_Compound, theOpened: TopoDS_Compound, theIgnore1DSubShape: bool) -> None: ...
	@staticmethod
	def FillFaceBoundaries(self, theShape: TopoDS_Shape, theUpperContinuity: Optional[GeomAbs_Shape]) -> Graphic3d_ArrayOfSegments: ...
	@staticmethod
	def FillTriangles(self, theShape: TopoDS_Shape) -> Graphic3d_ArrayOfTriangles: ...
	@staticmethod
	def FillTriangles(self, theShape: TopoDS_Shape, theHasTexels: bool, theUVOrigin: gp_Pnt2d, theUVRepeat: gp_Pnt2d, theUVScale: gp_Pnt2d) -> Graphic3d_ArrayOfTriangles: ...

class StdPrs_ShadedSurface(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aSurface: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> None: ...

class StdPrs_ToolPoint:
	@staticmethod
	def Coord(self, aPoint: Geom_Point) -> Tuple[float, float, float]: ...

class StdPrs_ToolRFace:
	def __init__(self) -> None: ...
	def __init__(self, aSurface: BRepAdaptor_HSurface) -> None: ...
	def Init(self) -> None: ...
	def IsInvalidGeometry(self) -> bool: ...
	def IsOriented(self) -> bool: ...
	def More(self) -> bool: ...
	def Next(self) -> None: ...
	def Orientation(self) -> TopAbs_Orientation: ...
	def Value(self) -> Adaptor2d_Curve2d: ...

class StdPrs_ToolTriangulatedShape:
	@staticmethod
	def ClearOnOwnDeflectionChange(self, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theToResetCoeff: bool) -> None: ...
	@staticmethod
	def ComputeNormals(self, theFace: TopoDS_Face, theTris: Poly_Triangulation) -> None: ...
	@staticmethod
	def ComputeNormals(self, theFace: TopoDS_Face, theTris: Poly_Triangulation, thePolyConnect: Poly_Connect) -> None: ...
	@staticmethod
	def IsClosed(self, theShape: TopoDS_Shape) -> bool: ...
	@staticmethod
	def IsTessellated(self, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def IsTriangulated(self, theShape: TopoDS_Shape) -> bool: ...
	@staticmethod
	def Normal(self, theFace: TopoDS_Face, thePolyConnect: Poly_Connect, theNormals: TColgp_Array1OfDir) -> None: ...
	@staticmethod
	def Tessellate(self, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> bool: ...

class StdPrs_ToolVertex:
	@staticmethod
	def Coord(self, aPoint: TopoDS_Vertex) -> Tuple[float, float, float]: ...

class StdPrs_WFDeflectionRestrictedFace(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aFace: BRepAdaptor_HSurface, aDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aFace: BRepAdaptor_HSurface, DrawUIso: bool, DrawVIso: bool, Deflection: float, NBUiso: int, NBViso: int, aDrawer: Prs3d_Drawer, Curves: Prs3d_NListOfSequenceOfPnt) -> None: ...
	@staticmethod
	def AddUIso(self, aPresentation: Prs3d_Presentation, aFace: BRepAdaptor_HSurface, aDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def AddVIso(self, aPresentation: Prs3d_Presentation, aFace: BRepAdaptor_HSurface, aDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def Match(self, X: float, Y: float, Z: float, aDistance: float, aFace: BRepAdaptor_HSurface, aDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def Match(self, X: float, Y: float, Z: float, aDistance: float, aFace: BRepAdaptor_HSurface, aDrawer: Prs3d_Drawer, DrawUIso: bool, DrawVIso: bool, aDeflection: float, NBUiso: int, NBViso: int) -> bool: ...
	@staticmethod
	def MatchUIso(self, X: float, Y: float, Z: float, aDistance: float, aFace: BRepAdaptor_HSurface, aDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def MatchVIso(self, X: float, Y: float, Z: float, aDistance: float, aFace: BRepAdaptor_HSurface, aDrawer: Prs3d_Drawer) -> bool: ...

class StdPrs_WFDeflectionSurface(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aSurface: Adaptor3d_HSurface, aDrawer: Prs3d_Drawer) -> None: ...

class StdPrs_WFPoleSurface(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aSurface: Adaptor3d_Surface, aDrawer: Prs3d_Drawer) -> None: ...

class StdPrs_WFRestrictedFace(Prs3d_Root):
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theFace: BRepAdaptor_HSurface, theDrawUIso: bool, theDrawVIso: bool, theNbUIso: int, theNbVIso: int, theDrawer: Prs3d_Drawer, theCurves: Prs3d_NListOfSequenceOfPnt) -> None: ...
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theFace: BRepAdaptor_HSurface, theDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def AddUIso(self, thePresentation: Prs3d_Presentation, theFace: BRepAdaptor_HSurface, theDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def AddVIso(self, thePresentation: Prs3d_Presentation, theFace: BRepAdaptor_HSurface, theDrawer: Prs3d_Drawer) -> None: ...
	@staticmethod
	def Match(self, theX: float, theY: float, theZ: float, theDistance: float, theFace: BRepAdaptor_HSurface, theDrawUIso: bool, theDrawVIso: bool, theDeflection: float, theNbUIso: int, theNbVIso: int, theDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def Match(self, theX: float, theY: float, theZ: float, theDistance: float, theFace: BRepAdaptor_HSurface, theDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def MatchUIso(self, theX: float, theY: float, theZ: float, theDistance: float, theFace: BRepAdaptor_HSurface, theDrawer: Prs3d_Drawer) -> bool: ...
	@staticmethod
	def MatchVIso(self, theX: float, theY: float, theZ: float, theDistance: float, theFace: BRepAdaptor_HSurface, theDrawer: Prs3d_Drawer) -> bool: ...

class StdPrs_WFShape(Prs3d_Root):
	@staticmethod
	def Add(self, thePresentation: Prs3d_Presentation, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer, theIsParallel: Optional[bool]) -> None: ...
	@staticmethod
	def AddAllEdges(self, theShape: TopoDS_Shape, theDrawer: Prs3d_Drawer) -> Graphic3d_ArrayOfPrimitives: ...
	@staticmethod
	def AddEdgesOnTriangulation(self, theShape: TopoDS_Shape, theToExcludeGeometric: Optional[bool]) -> Graphic3d_ArrayOfPrimitives: ...
	@staticmethod
	def AddEdgesOnTriangulation(self, theSegments: TColgp_SequenceOfPnt, theShape: TopoDS_Shape, theToExcludeGeometric: Optional[bool]) -> None: ...
	@staticmethod
	def AddVertexes(self, theShape: TopoDS_Shape, theVertexMode: Prs3d_VertexDrawMode) -> Graphic3d_ArrayOfPoints: ...

class StdPrs_WFSurface(Prs3d_Root):
	@staticmethod
	def Add(self, aPresentation: Prs3d_Presentation, aSurface: Adaptor3d_HSurface, aDrawer: Prs3d_Drawer) -> None: ...
