from typing import NewType, Optional, Tuple

from OCC.Core.BRepFilletAPI import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.BRepBuilderAPI import *
from OCC.Core.TopoDS import *
from OCC.Core.ChFiDS import *
from OCC.Core.TopTools import *
from OCC.Core.ChFi2d import *
from OCC.Core.TopOpeBRepBuild import *
from OCC.Core.ChFi3d import *
from OCC.Core.Law import *
from OCC.Core.TColgp import *
from OCC.Core.Geom import *
from OCC.Core.GeomAbs import *


class BRepFilletAPI_LocalOperation(BRepBuilderAPI_MakeShape):
	def Abscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
	def Add(self, E: TopoDS_Edge) -> None: ...
	def Closed(self, IC: int) -> bool: ...
	def ClosedAndTangent(self, IC: int) -> bool: ...
	def Contour(self, E: TopoDS_Edge) -> int: ...
	def Edge(self, I: int, J: int) -> TopoDS_Edge: ...
	def FirstVertex(self, IC: int) -> TopoDS_Vertex: ...
	def LastVertex(self, IC: int) -> TopoDS_Vertex: ...
	def Length(self, IC: int) -> float: ...
	def NbContours(self) -> int: ...
	def NbEdges(self, I: int) -> int: ...
	def NbSurf(self, IC: int) -> int: ...
	def RelativeAbscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
	def Remove(self, E: TopoDS_Edge) -> None: ...
	def Reset(self) -> None: ...
	def ResetContour(self, IC: int) -> None: ...
	def Sect(self, IC: int, IS: int) -> ChFiDS_SecHArray1: ...
	def Simulate(self, IC: int) -> None: ...

class BRepFilletAPI_MakeFillet2d(BRepBuilderAPI_MakeShape):
	def __init__(self) -> None: ...
	def __init__(self, F: TopoDS_Face) -> None: ...
	def AddChamfer(self, E1: TopoDS_Edge, E2: TopoDS_Edge, D1: float, D2: float) -> TopoDS_Edge: ...
	def AddChamfer(self, E: TopoDS_Edge, V: TopoDS_Vertex, D: float, Ang: float) -> TopoDS_Edge: ...
	def AddFillet(self, V: TopoDS_Vertex, Radius: float) -> TopoDS_Edge: ...
	def BasisEdge(self, E: TopoDS_Edge) -> TopoDS_Edge: ...
	def Build(self) -> None: ...
	def ChamferEdges(self) -> TopTools_SequenceOfShape: ...
	def DescendantEdge(self, E: TopoDS_Edge) -> TopoDS_Edge: ...
	def FilletEdges(self) -> TopTools_SequenceOfShape: ...
	def HasDescendant(self, E: TopoDS_Edge) -> bool: ...
	def Init(self, F: TopoDS_Face) -> None: ...
	def Init(self, RefFace: TopoDS_Face, ModFace: TopoDS_Face) -> None: ...
	def IsModified(self, E: TopoDS_Edge) -> bool: ...
	def Modified(self, S: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def ModifyChamfer(self, Chamfer: TopoDS_Edge, E1: TopoDS_Edge, E2: TopoDS_Edge, D1: float, D2: float) -> TopoDS_Edge: ...
	def ModifyChamfer(self, Chamfer: TopoDS_Edge, E: TopoDS_Edge, D: float, Ang: float) -> TopoDS_Edge: ...
	def ModifyFillet(self, Fillet: TopoDS_Edge, Radius: float) -> TopoDS_Edge: ...
	def NbChamfer(self) -> int: ...
	def NbCurves(self) -> int: ...
	def NbFillet(self) -> int: ...
	def NewEdges(self, I: int) -> TopTools_ListOfShape: ...
	def RemoveChamfer(self, Chamfer: TopoDS_Edge) -> TopoDS_Vertex: ...
	def RemoveFillet(self, Fillet: TopoDS_Edge) -> TopoDS_Vertex: ...
	def Status(self) -> ChFi2d_ConstructionError: ...

class BRepFilletAPI_MakeChamfer(BRepFilletAPI_LocalOperation):
	def __init__(self, S: TopoDS_Shape) -> None: ...
	def Abscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
	def Add(self, E: TopoDS_Edge) -> None: ...
	def Add(self, Dis: float, E: TopoDS_Edge) -> None: ...
	def Add(self, Dis1: float, Dis2: float, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def AddDA(self, Dis: float, Angle: float, E: TopoDS_Edge, F: TopoDS_Face) -> None: ...
	def Build(self) -> None: ...
	def Builder(self) -> TopOpeBRepBuild_HBuilder: ...
	def Closed(self, IC: int) -> bool: ...
	def ClosedAndTangent(self, IC: int) -> bool: ...
	def Contour(self, E: TopoDS_Edge) -> int: ...
	def Dists(self, IC: int) -> Tuple[float, float]: ...
	def Edge(self, I: int, J: int) -> TopoDS_Edge: ...
	def FirstVertex(self, IC: int) -> TopoDS_Vertex: ...
	def Generated(self, EorV: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def GetDist(self, IC: int) -> float: ...
	def GetDistAngle(self, IC: int) -> Tuple[float, float]: ...
	def IsDeleted(self, F: TopoDS_Shape) -> bool: ...
	def IsDistanceAngle(self, IC: int) -> bool: ...
	def IsSymetric(self, IC: int) -> bool: ...
	def IsTwoDistances(self, IC: int) -> bool: ...
	def LastVertex(self, IC: int) -> TopoDS_Vertex: ...
	def Length(self, IC: int) -> float: ...
	def Modified(self, F: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def NbContours(self) -> int: ...
	def NbEdges(self, I: int) -> int: ...
	def NbSurf(self, IC: int) -> int: ...
	def RelativeAbscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
	def Remove(self, E: TopoDS_Edge) -> None: ...
	def Reset(self) -> None: ...
	def ResetContour(self, IC: int) -> None: ...
	def Sect(self, IC: int, IS: int) -> ChFiDS_SecHArray1: ...
	def SetDist(self, Dis: float, IC: int, F: TopoDS_Face) -> None: ...
	def SetDistAngle(self, Dis: float, Angle: float, IC: int, F: TopoDS_Face) -> None: ...
	def SetDists(self, Dis1: float, Dis2: float, IC: int, F: TopoDS_Face) -> None: ...
	def SetMode(self, theMode: ChFiDS_ChamfMode) -> None: ...
	def Simulate(self, IC: int) -> None: ...

class BRepFilletAPI_MakeFillet(BRepFilletAPI_LocalOperation):
	def __init__(self, S: TopoDS_Shape, FShape: Optional[ChFi3d_FilletShape]) -> None: ...
	def Abscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
	def Add(self, E: TopoDS_Edge) -> None: ...
	def Add(self, Radius: float, E: TopoDS_Edge) -> None: ...
	def Add(self, R1: float, R2: float, E: TopoDS_Edge) -> None: ...
	def Add(self, L: Law_Function, E: TopoDS_Edge) -> None: ...
	def Add(self, UandR: TColgp_Array1OfPnt2d, E: TopoDS_Edge) -> None: ...
	def BadShape(self) -> TopoDS_Shape: ...
	def Build(self) -> None: ...
	def Builder(self) -> TopOpeBRepBuild_HBuilder: ...
	def Closed(self, IC: int) -> bool: ...
	def ClosedAndTangent(self, IC: int) -> bool: ...
	def ComputedSurface(self, IC: int, IS: int) -> Geom_Surface: ...
	def Contour(self, E: TopoDS_Edge) -> int: ...
	def Edge(self, I: int, J: int) -> TopoDS_Edge: ...
	def FaultyContour(self, I: int) -> int: ...
	def FaultyVertex(self, IV: int) -> TopoDS_Vertex: ...
	def FirstVertex(self, IC: int) -> TopoDS_Vertex: ...
	def Generated(self, EorV: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def GetBounds(self, IC: int, E: TopoDS_Edge) -> Tuple[bool, float, float]: ...
	def GetFilletShape(self) -> ChFi3d_FilletShape: ...
	def GetLaw(self, IC: int, E: TopoDS_Edge) -> Law_Function: ...
	def HasResult(self) -> bool: ...
	def IsConstant(self, IC: int) -> bool: ...
	def IsConstant(self, IC: int, E: TopoDS_Edge) -> bool: ...
	def IsDeleted(self, F: TopoDS_Shape) -> bool: ...
	def LastVertex(self, IC: int) -> TopoDS_Vertex: ...
	def Length(self, IC: int) -> float: ...
	def Modified(self, F: TopoDS_Shape) -> TopTools_ListOfShape: ...
	def NbComputedSurfaces(self, IC: int) -> int: ...
	def NbContours(self) -> int: ...
	def NbEdges(self, I: int) -> int: ...
	def NbFaultyContours(self) -> int: ...
	def NbFaultyVertices(self) -> int: ...
	def NbSurf(self, IC: int) -> int: ...
	def NbSurfaces(self) -> int: ...
	def NewFaces(self, I: int) -> TopTools_ListOfShape: ...
	def Radius(self, IC: int) -> float: ...
	def Radius(self, IC: int, E: TopoDS_Edge) -> float: ...
	def RelativeAbscissa(self, IC: int, V: TopoDS_Vertex) -> float: ...
	def Remove(self, E: TopoDS_Edge) -> None: ...
	def Reset(self) -> None: ...
	def ResetContour(self, IC: int) -> None: ...
	def Sect(self, IC: int, IS: int) -> ChFiDS_SecHArray1: ...
	def SetContinuity(self, InternalContinuity: GeomAbs_Shape, AngularTolerance: float) -> None: ...
	def SetFilletShape(self, FShape: ChFi3d_FilletShape) -> None: ...
	def SetLaw(self, IC: int, E: TopoDS_Edge, L: Law_Function) -> None: ...
	def SetParams(self, Tang: float, Tesp: float, T2d: float, TApp3d: float, TolApp2d: float, Fleche: float) -> None: ...
	def SetRadius(self, Radius: float, IC: int, IinC: int) -> None: ...
	def SetRadius(self, R1: float, R2: float, IC: int, IinC: int) -> None: ...
	def SetRadius(self, L: Law_Function, IC: int, IinC: int) -> None: ...
	def SetRadius(self, UandR: TColgp_Array1OfPnt2d, IC: int, IinC: int) -> None: ...
	def SetRadius(self, Radius: float, IC: int, E: TopoDS_Edge) -> None: ...
	def SetRadius(self, Radius: float, IC: int, V: TopoDS_Vertex) -> None: ...
	def Simulate(self, IC: int) -> None: ...
	def StripeStatus(self, IC: int) -> ChFiDS_ErrorStatus: ...
