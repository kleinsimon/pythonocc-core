from typing import NewType, Optional, Tuple

from OCC.Core.StepFEA import *
from OCC.Core.Standard import *
from OCC.Core.NCollection import *
from OCC.Core.TCollection import *
from OCC.Core.StepData import *
from OCC.Core.TColStd import *
from OCC.Core.StepElement import *
from OCC.Core.StepBasic import *
from OCC.Core.StepRepr import *
from OCC.Core.StepGeom import *


class StepFEA_ElementVolume:
	StepFEA_Volume: int = ...

class StepFEA_CoordinateSystemType:
	StepFEA_Cartesian: int = ...
	StepFEA_Cylindrical: int = ...
	StepFEA_Spherical: int = ...

class StepFEA_EnumeratedDegreeOfFreedom:
	StepFEA_XTranslation: int = ...
	StepFEA_YTranslation: int = ...
	StepFEA_ZTranslation: int = ...
	StepFEA_XRotation: int = ...
	StepFEA_YRotation: int = ...
	StepFEA_ZRotation: int = ...
	StepFEA_Warp: int = ...

class StepFEA_CurveEdge:
	StepFEA_ElementEdge: int = ...

class StepFEA_UnspecifiedValue:
	StepFEA_Unspecified: int = ...

class StepFEA_Curve3dElementProperty(Standard_Transient):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def EndOffsets(self) -> StepFEA_HArray1OfCurveElementEndOffset: ...
	def EndReleases(self) -> StepFEA_HArray1OfCurveElementEndRelease: ...
	def Init(self, aPropertyId: TCollection_HAsciiString, aDescription: TCollection_HAsciiString, aIntervalDefinitions: StepFEA_HArray1OfCurveElementInterval, aEndOffsets: StepFEA_HArray1OfCurveElementEndOffset, aEndReleases: StepFEA_HArray1OfCurveElementEndRelease) -> None: ...
	def IntervalDefinitions(self) -> StepFEA_HArray1OfCurveElementInterval: ...
	def PropertyId(self) -> TCollection_HAsciiString: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetEndOffsets(self, EndOffsets: StepFEA_HArray1OfCurveElementEndOffset) -> None: ...
	def SetEndReleases(self, EndReleases: StepFEA_HArray1OfCurveElementEndRelease) -> None: ...
	def SetIntervalDefinitions(self, IntervalDefinitions: StepFEA_HArray1OfCurveElementInterval) -> None: ...
	def SetPropertyId(self, PropertyId: TCollection_HAsciiString) -> None: ...

class StepFEA_CurveElementEndCoordinateSystem(StepData_SelectType):
	def __init__(self) -> None: ...
	def AlignedCurve3dElementCoordinateSystem(self) -> StepFEA_AlignedCurve3dElementCoordinateSystem: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def FeaAxis2Placement3d(self) -> StepFEA_FeaAxis2Placement3d: ...
	def ParametricCurve3dElementCoordinateSystem(self) -> StepFEA_ParametricCurve3dElementCoordinateSystem: ...

class StepFEA_CurveElementEndOffset(Standard_Transient):
	def __init__(self) -> None: ...
	def CoordinateSystem(self) -> StepFEA_CurveElementEndCoordinateSystem: ...
	def Init(self, aCoordinateSystem: StepFEA_CurveElementEndCoordinateSystem, aOffsetVector: TColStd_HArray1OfReal) -> None: ...
	def OffsetVector(self) -> TColStd_HArray1OfReal: ...
	def SetCoordinateSystem(self, CoordinateSystem: StepFEA_CurveElementEndCoordinateSystem) -> None: ...
	def SetOffsetVector(self, OffsetVector: TColStd_HArray1OfReal) -> None: ...

class StepFEA_CurveElementEndRelease(Standard_Transient):
	def __init__(self) -> None: ...
	def CoordinateSystem(self) -> StepFEA_CurveElementEndCoordinateSystem: ...
	def Init(self, aCoordinateSystem: StepFEA_CurveElementEndCoordinateSystem, aReleases: StepElement_HArray1OfCurveElementEndReleasePacket) -> None: ...
	def Releases(self) -> StepElement_HArray1OfCurveElementEndReleasePacket: ...
	def SetCoordinateSystem(self, CoordinateSystem: StepFEA_CurveElementEndCoordinateSystem) -> None: ...
	def SetReleases(self, Releases: StepElement_HArray1OfCurveElementEndReleasePacket) -> None: ...

class StepFEA_CurveElementInterval(Standard_Transient):
	def __init__(self) -> None: ...
	def EuAngles(self) -> StepBasic_EulerAngles: ...
	def FinishPosition(self) -> StepFEA_CurveElementLocation: ...
	def Init(self, aFinishPosition: StepFEA_CurveElementLocation, aEuAngles: StepBasic_EulerAngles) -> None: ...
	def SetEuAngles(self, EuAngles: StepBasic_EulerAngles) -> None: ...
	def SetFinishPosition(self, FinishPosition: StepFEA_CurveElementLocation) -> None: ...

class StepFEA_CurveElementLocation(Standard_Transient):
	def __init__(self) -> None: ...
	def Coordinate(self) -> StepFEA_FeaParametricPoint: ...
	def Init(self, aCoordinate: StepFEA_FeaParametricPoint) -> None: ...
	def SetCoordinate(self, Coordinate: StepFEA_FeaParametricPoint) -> None: ...

class StepFEA_DegreeOfFreedom(StepData_SelectType):
	def __init__(self) -> None: ...
	def ApplicationDefinedDegreeOfFreedom(self) -> TCollection_HAsciiString: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def EnumeratedDegreeOfFreedom(self) -> StepFEA_EnumeratedDegreeOfFreedom: ...
	def NewMember(self) -> StepData_SelectMember: ...
	def SetApplicationDefinedDegreeOfFreedom(self, aVal: TCollection_HAsciiString) -> None: ...
	def SetEnumeratedDegreeOfFreedom(self, aVal: StepFEA_EnumeratedDegreeOfFreedom) -> None: ...

class StepFEA_DegreeOfFreedomMember(StepData_SelectNamed):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepFEA_ElementGeometricRelationship(Standard_Transient):
	def __init__(self) -> None: ...
	def Aspect(self) -> StepElement_ElementAspect: ...
	def ElementRef(self) -> StepFEA_ElementOrElementGroup: ...
	def Init(self, aElementRef: StepFEA_ElementOrElementGroup, aItem: StepElement_AnalysisItemWithinRepresentation, aAspect: StepElement_ElementAspect) -> None: ...
	def Item(self) -> StepElement_AnalysisItemWithinRepresentation: ...
	def SetAspect(self, Aspect: StepElement_ElementAspect) -> None: ...
	def SetElementRef(self, ElementRef: StepFEA_ElementOrElementGroup) -> None: ...
	def SetItem(self, Item: StepElement_AnalysisItemWithinRepresentation) -> None: ...

class StepFEA_ElementOrElementGroup(StepData_SelectType):
	def __init__(self) -> None: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def ElementGroup(self) -> StepFEA_ElementGroup: ...
	def ElementRepresentation(self) -> StepFEA_ElementRepresentation: ...

class StepFEA_ElementRepresentation(StepRepr_Representation):
	def __init__(self) -> None: ...
	def Init(self, aRepresentation_Name: TCollection_HAsciiString, aRepresentation_Items: StepRepr_HArray1OfRepresentationItem, aRepresentation_ContextOfItems: StepRepr_RepresentationContext, aNodeList: StepFEA_HArray1OfNodeRepresentation) -> None: ...
	def NodeList(self) -> StepFEA_HArray1OfNodeRepresentation: ...
	def SetNodeList(self, NodeList: StepFEA_HArray1OfNodeRepresentation) -> None: ...

class StepFEA_FeaAxis2Placement3d(StepGeom_Axis2Placement3d):
	def __init__(self) -> None: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aPlacement_Location: StepGeom_CartesianPoint, hasAxis2Placement3d_Axis: bool, aAxis2Placement3d_Axis: StepGeom_Direction, hasAxis2Placement3d_RefDirection: bool, aAxis2Placement3d_RefDirection: StepGeom_Direction, aSystemType: StepFEA_CoordinateSystemType, aDescription: TCollection_HAsciiString) -> None: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetSystemType(self, SystemType: StepFEA_CoordinateSystemType) -> None: ...
	def SystemType(self) -> StepFEA_CoordinateSystemType: ...

class StepFEA_FeaCurveSectionGeometricRelationship(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aSectionRef: StepElement_CurveElementSectionDefinition, aItem: StepElement_AnalysisItemWithinRepresentation) -> None: ...
	def Item(self) -> StepElement_AnalysisItemWithinRepresentation: ...
	def SectionRef(self) -> StepElement_CurveElementSectionDefinition: ...
	def SetItem(self, Item: StepElement_AnalysisItemWithinRepresentation) -> None: ...
	def SetSectionRef(self, SectionRef: StepElement_CurveElementSectionDefinition) -> None: ...

class StepFEA_FeaGroup(StepBasic_Group):
	def __init__(self) -> None: ...
	def Init(self, aGroup_Name: TCollection_HAsciiString, aGroup_Description: TCollection_HAsciiString, aModelRef: StepFEA_FeaModel) -> None: ...
	def ModelRef(self) -> StepFEA_FeaModel: ...
	def SetModelRef(self, ModelRef: StepFEA_FeaModel) -> None: ...

class StepFEA_FeaMaterialPropertyRepresentation(StepRepr_MaterialPropertyRepresentation):
	def __init__(self) -> None: ...

class StepFEA_FeaMaterialPropertyRepresentationItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...

class StepFEA_FeaModel(StepRepr_Representation):
	def __init__(self) -> None: ...
	def AnalysisType(self) -> TCollection_HAsciiString: ...
	def CreatingSoftware(self) -> TCollection_HAsciiString: ...
	def Description(self) -> TCollection_HAsciiString: ...
	def Init(self, aRepresentation_Name: TCollection_HAsciiString, aRepresentation_Items: StepRepr_HArray1OfRepresentationItem, aRepresentation_ContextOfItems: StepRepr_RepresentationContext, aCreatingSoftware: TCollection_HAsciiString, aIntendedAnalysisCode: TColStd_HArray1OfAsciiString, aDescription: TCollection_HAsciiString, aAnalysisType: TCollection_HAsciiString) -> None: ...
	def IntendedAnalysisCode(self) -> TColStd_HArray1OfAsciiString: ...
	def SetAnalysisType(self, AnalysisType: TCollection_HAsciiString) -> None: ...
	def SetCreatingSoftware(self, CreatingSoftware: TCollection_HAsciiString) -> None: ...
	def SetDescription(self, Description: TCollection_HAsciiString) -> None: ...
	def SetIntendedAnalysisCode(self, IntendedAnalysisCode: TColStd_HArray1OfAsciiString) -> None: ...

class StepFEA_FeaModelDefinition(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...

class StepFEA_FeaParametricPoint(StepGeom_Point):
	def __init__(self) -> None: ...
	def Coordinates(self) -> TColStd_HArray1OfReal: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aCoordinates: TColStd_HArray1OfReal) -> None: ...
	def SetCoordinates(self, Coordinates: TColStd_HArray1OfReal) -> None: ...

class StepFEA_FeaRepresentationItem(StepRepr_RepresentationItem):
	def __init__(self) -> None: ...

class StepFEA_FeaSurfaceSectionGeometricRelationship(Standard_Transient):
	def __init__(self) -> None: ...
	def Init(self, aSectionRef: StepElement_SurfaceSection, aItem: StepElement_AnalysisItemWithinRepresentation) -> None: ...
	def Item(self) -> StepElement_AnalysisItemWithinRepresentation: ...
	def SectionRef(self) -> StepElement_SurfaceSection: ...
	def SetItem(self, Item: StepElement_AnalysisItemWithinRepresentation) -> None: ...
	def SetSectionRef(self, SectionRef: StepElement_SurfaceSection) -> None: ...

class StepFEA_FreedomAndCoefficient(Standard_Transient):
	def __init__(self) -> None: ...
	def A(self) -> StepElement_MeasureOrUnspecifiedValue: ...
	def Freedom(self) -> StepFEA_DegreeOfFreedom: ...
	def Init(self, aFreedom: StepFEA_DegreeOfFreedom, aA: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetA(self, A: StepElement_MeasureOrUnspecifiedValue) -> None: ...
	def SetFreedom(self, Freedom: StepFEA_DegreeOfFreedom) -> None: ...

class StepFEA_FreedomsList(Standard_Transient):
	def __init__(self) -> None: ...
	def Freedoms(self) -> StepFEA_HArray1OfDegreeOfFreedom: ...
	def Init(self, aFreedoms: StepFEA_HArray1OfDegreeOfFreedom) -> None: ...
	def SetFreedoms(self, Freedoms: StepFEA_HArray1OfDegreeOfFreedom) -> None: ...

class StepFEA_NodeDefinition(StepRepr_ShapeAspect):
	def __init__(self) -> None: ...

class StepFEA_NodeRepresentation(StepRepr_Representation):
	def __init__(self) -> None: ...
	def Init(self, aRepresentation_Name: TCollection_HAsciiString, aRepresentation_Items: StepRepr_HArray1OfRepresentationItem, aRepresentation_ContextOfItems: StepRepr_RepresentationContext, aModelRef: StepFEA_FeaModel) -> None: ...
	def ModelRef(self) -> StepFEA_FeaModel: ...
	def SetModelRef(self, ModelRef: StepFEA_FeaModel) -> None: ...

class StepFEA_NodeSet(StepGeom_GeometricRepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aNodes: StepFEA_HArray1OfNodeRepresentation) -> None: ...
	def Nodes(self) -> StepFEA_HArray1OfNodeRepresentation: ...
	def SetNodes(self, Nodes: StepFEA_HArray1OfNodeRepresentation) -> None: ...

class StepFEA_SymmetricTensor22d(StepData_SelectType):
	def __init__(self) -> None: ...
	def AnisotropicSymmetricTensor22d(self) -> TColStd_HArray1OfReal: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...

class StepFEA_SymmetricTensor23d(StepData_SelectType):
	def __init__(self) -> None: ...
	def AnisotropicSymmetricTensor23d(self) -> TColStd_HArray1OfReal: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def IsotropicSymmetricTensor23d(self) -> float: ...
	def NewMember(self) -> StepData_SelectMember: ...
	def OrthotropicSymmetricTensor23d(self) -> TColStd_HArray1OfReal: ...
	def SetAnisotropicSymmetricTensor23d(self, aVal: TColStd_HArray1OfReal) -> None: ...
	def SetIsotropicSymmetricTensor23d(self, aVal: float) -> None: ...
	def SetOrthotropicSymmetricTensor23d(self, aVal: TColStd_HArray1OfReal) -> None: ...

class StepFEA_SymmetricTensor23dMember(StepData_SelectArrReal):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepFEA_SymmetricTensor42d(StepData_SelectType):
	def __init__(self) -> None: ...
	def AnisotropicSymmetricTensor42d(self) -> TColStd_HArray1OfReal: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...

class StepFEA_SymmetricTensor43d(StepData_SelectType):
	def __init__(self) -> None: ...
	def AnisotropicSymmetricTensor43d(self) -> TColStd_HArray1OfReal: ...
	def CaseMem(self, ent: StepData_SelectMember) -> int: ...
	def CaseNum(self, ent: Standard_Transient) -> int: ...
	def FeaColumnNormalisedMonoclinicSymmetricTensor43d(self) -> TColStd_HArray1OfReal: ...
	def FeaColumnNormalisedOrthotropicSymmetricTensor43d(self) -> TColStd_HArray1OfReal: ...
	def FeaIsoOrthotropicSymmetricTensor43d(self) -> TColStd_HArray1OfReal: ...
	def FeaIsotropicSymmetricTensor43d(self) -> TColStd_HArray1OfReal: ...
	def FeaTransverseIsotropicSymmetricTensor43d(self) -> TColStd_HArray1OfReal: ...
	def NewMember(self) -> StepData_SelectMember: ...

class StepFEA_SymmetricTensor43dMember(StepData_SelectArrReal):
	def __init__(self) -> None: ...
	def HasName(self) -> bool: ...
	def Matches(self, name: str) -> bool: ...
	def Name(self) -> str: ...
	def SetName(self, name: str) -> bool: ...

class StepFEA_AlignedCurve3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
	def __init__(self) -> None: ...
	def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aCoordinateSystem: StepFEA_FeaAxis2Placement3d) -> None: ...
	def SetCoordinateSystem(self, CoordinateSystem: StepFEA_FeaAxis2Placement3d) -> None: ...

class StepFEA_AlignedSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
	def __init__(self) -> None: ...
	def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aCoordinateSystem: StepFEA_FeaAxis2Placement3d) -> None: ...
	def SetCoordinateSystem(self, CoordinateSystem: StepFEA_FeaAxis2Placement3d) -> None: ...

class StepFEA_ArbitraryVolume3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
	def __init__(self) -> None: ...
	def CoordinateSystem(self) -> StepFEA_FeaAxis2Placement3d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aCoordinateSystem: StepFEA_FeaAxis2Placement3d) -> None: ...
	def SetCoordinateSystem(self, CoordinateSystem: StepFEA_FeaAxis2Placement3d) -> None: ...

class StepFEA_ConstantSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
	def __init__(self) -> None: ...
	def Angle(self) -> float: ...
	def Axis(self) -> int: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aAxis: int, aAngle: float) -> None: ...
	def SetAngle(self, Angle: float) -> None: ...
	def SetAxis(self, Axis: int) -> None: ...

class StepFEA_Curve3dElementRepresentation(StepFEA_ElementRepresentation):
	def __init__(self) -> None: ...
	def ElementDescriptor(self) -> StepElement_Curve3dElementDescriptor: ...
	def Init(self, aRepresentation_Name: TCollection_HAsciiString, aRepresentation_Items: StepRepr_HArray1OfRepresentationItem, aRepresentation_ContextOfItems: StepRepr_RepresentationContext, aElementRepresentation_NodeList: StepFEA_HArray1OfNodeRepresentation, aModelRef: StepFEA_FeaModel3d, aElementDescriptor: StepElement_Curve3dElementDescriptor, aProperty: StepFEA_Curve3dElementProperty, aMaterial: StepElement_ElementMaterial) -> None: ...
	def Material(self) -> StepElement_ElementMaterial: ...
	def ModelRef(self) -> StepFEA_FeaModel3d: ...
	def Property(self) -> StepFEA_Curve3dElementProperty: ...
	def SetElementDescriptor(self, ElementDescriptor: StepElement_Curve3dElementDescriptor) -> None: ...
	def SetMaterial(self, Material: StepElement_ElementMaterial) -> None: ...
	def SetModelRef(self, ModelRef: StepFEA_FeaModel3d) -> None: ...
	def SetProperty(self, Property: StepFEA_Curve3dElementProperty) -> None: ...

class StepFEA_CurveElementIntervalConstant(StepFEA_CurveElementInterval):
	def __init__(self) -> None: ...
	def Init(self, aCurveElementInterval_FinishPosition: StepFEA_CurveElementLocation, aCurveElementInterval_EuAngles: StepBasic_EulerAngles, aSection: StepElement_CurveElementSectionDefinition) -> None: ...
	def Section(self) -> StepElement_CurveElementSectionDefinition: ...
	def SetSection(self, Section: StepElement_CurveElementSectionDefinition) -> None: ...

class StepFEA_CurveElementIntervalLinearlyVarying(StepFEA_CurveElementInterval):
	def __init__(self) -> None: ...
	def Init(self, aCurveElementInterval_FinishPosition: StepFEA_CurveElementLocation, aCurveElementInterval_EuAngles: StepBasic_EulerAngles, aSections: StepElement_HArray1OfCurveElementSectionDefinition) -> None: ...
	def Sections(self) -> StepElement_HArray1OfCurveElementSectionDefinition: ...
	def SetSections(self, Sections: StepElement_HArray1OfCurveElementSectionDefinition) -> None: ...

class StepFEA_DummyNode(StepFEA_NodeRepresentation):
	def __init__(self) -> None: ...

class StepFEA_ElementGroup(StepFEA_FeaGroup):
	def __init__(self) -> None: ...
	def Elements(self) -> StepFEA_HArray1OfElementRepresentation: ...
	def Init(self, aGroup_Name: TCollection_HAsciiString, aGroup_Description: TCollection_HAsciiString, aFeaGroup_ModelRef: StepFEA_FeaModel, aElements: StepFEA_HArray1OfElementRepresentation) -> None: ...
	def SetElements(self, Elements: StepFEA_HArray1OfElementRepresentation) -> None: ...

class StepFEA_FeaAreaDensity(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstant(self) -> float: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstant: float) -> None: ...
	def SetFeaConstant(self, FeaConstant: float) -> None: ...

class StepFEA_FeaLinearElasticity(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstants(self) -> StepFEA_SymmetricTensor43d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstants: StepFEA_SymmetricTensor43d) -> None: ...
	def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor43d) -> None: ...

class StepFEA_FeaMassDensity(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstant(self) -> float: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstant: float) -> None: ...
	def SetFeaConstant(self, FeaConstant: float) -> None: ...

class StepFEA_FeaModel3d(StepFEA_FeaModel):
	def __init__(self) -> None: ...

class StepFEA_FeaMoistureAbsorption(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstants(self) -> StepFEA_SymmetricTensor23d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstants: StepFEA_SymmetricTensor23d) -> None: ...
	def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor23d) -> None: ...

class StepFEA_FeaSecantCoefficientOfLinearThermalExpansion(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstants(self) -> StepFEA_SymmetricTensor23d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstants: StepFEA_SymmetricTensor23d, aReferenceTemperature: float) -> None: ...
	def ReferenceTemperature(self) -> float: ...
	def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor23d) -> None: ...
	def SetReferenceTemperature(self, ReferenceTemperature: float) -> None: ...

class StepFEA_FeaShellBendingStiffness(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstants(self) -> StepFEA_SymmetricTensor42d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstants: StepFEA_SymmetricTensor42d) -> None: ...
	def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor42d) -> None: ...

class StepFEA_FeaShellMembraneBendingCouplingStiffness(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstants(self) -> StepFEA_SymmetricTensor42d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstants: StepFEA_SymmetricTensor42d) -> None: ...
	def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor42d) -> None: ...

class StepFEA_FeaShellMembraneStiffness(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstants(self) -> StepFEA_SymmetricTensor42d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstants: StepFEA_SymmetricTensor42d) -> None: ...
	def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor42d) -> None: ...

class StepFEA_FeaShellShearStiffness(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstants(self) -> StepFEA_SymmetricTensor22d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstants: StepFEA_SymmetricTensor22d) -> None: ...
	def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor22d) -> None: ...

class StepFEA_FeaTangentialCoefficientOfLinearThermalExpansion(StepFEA_FeaMaterialPropertyRepresentationItem):
	def __init__(self) -> None: ...
	def FeaConstants(self) -> StepFEA_SymmetricTensor23d: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aFeaConstants: StepFEA_SymmetricTensor23d) -> None: ...
	def SetFeaConstants(self, FeaConstants: StepFEA_SymmetricTensor23d) -> None: ...

class StepFEA_GeometricNode(StepFEA_NodeRepresentation):
	def __init__(self) -> None: ...

class StepFEA_Node(StepFEA_NodeRepresentation):
	def __init__(self) -> None: ...

class StepFEA_NodeGroup(StepFEA_FeaGroup):
	def __init__(self) -> None: ...
	def Init(self, aGroup_Name: TCollection_HAsciiString, aGroup_Description: TCollection_HAsciiString, aFeaGroup_ModelRef: StepFEA_FeaModel, aNodes: StepFEA_HArray1OfNodeRepresentation) -> None: ...
	def Nodes(self) -> StepFEA_HArray1OfNodeRepresentation: ...
	def SetNodes(self, Nodes: StepFEA_HArray1OfNodeRepresentation) -> None: ...

class StepFEA_ParametricCurve3dElementCoordinateDirection(StepFEA_FeaRepresentationItem):
	def __init__(self) -> None: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aOrientation: StepGeom_Direction) -> None: ...
	def Orientation(self) -> StepGeom_Direction: ...
	def SetOrientation(self, Orientation: StepGeom_Direction) -> None: ...

class StepFEA_ParametricCurve3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
	def __init__(self) -> None: ...
	def Direction(self) -> StepFEA_ParametricCurve3dElementCoordinateDirection: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aDirection: StepFEA_ParametricCurve3dElementCoordinateDirection) -> None: ...
	def SetDirection(self, Direction: StepFEA_ParametricCurve3dElementCoordinateDirection) -> None: ...

class StepFEA_ParametricSurface3dElementCoordinateSystem(StepFEA_FeaRepresentationItem):
	def __init__(self) -> None: ...
	def Angle(self) -> float: ...
	def Axis(self) -> int: ...
	def Init(self, aRepresentationItem_Name: TCollection_HAsciiString, aAxis: int, aAngle: float) -> None: ...
	def SetAngle(self, Angle: float) -> None: ...
	def SetAxis(self, Axis: int) -> None: ...

class StepFEA_Surface3dElementRepresentation(StepFEA_ElementRepresentation):
	def __init__(self) -> None: ...
	def ElementDescriptor(self) -> StepElement_Surface3dElementDescriptor: ...
	def Init(self, aRepresentation_Name: TCollection_HAsciiString, aRepresentation_Items: StepRepr_HArray1OfRepresentationItem, aRepresentation_ContextOfItems: StepRepr_RepresentationContext, aElementRepresentation_NodeList: StepFEA_HArray1OfNodeRepresentation, aModelRef: StepFEA_FeaModel3d, aElementDescriptor: StepElement_Surface3dElementDescriptor, aProperty: StepElement_SurfaceElementProperty, aMaterial: StepElement_ElementMaterial) -> None: ...
	def Material(self) -> StepElement_ElementMaterial: ...
	def ModelRef(self) -> StepFEA_FeaModel3d: ...
	def Property(self) -> StepElement_SurfaceElementProperty: ...
	def SetElementDescriptor(self, ElementDescriptor: StepElement_Surface3dElementDescriptor) -> None: ...
	def SetMaterial(self, Material: StepElement_ElementMaterial) -> None: ...
	def SetModelRef(self, ModelRef: StepFEA_FeaModel3d) -> None: ...
	def SetProperty(self, Property: StepElement_SurfaceElementProperty) -> None: ...

class StepFEA_Volume3dElementRepresentation(StepFEA_ElementRepresentation):
	def __init__(self) -> None: ...
	def ElementDescriptor(self) -> StepElement_Volume3dElementDescriptor: ...
	def Init(self, aRepresentation_Name: TCollection_HAsciiString, aRepresentation_Items: StepRepr_HArray1OfRepresentationItem, aRepresentation_ContextOfItems: StepRepr_RepresentationContext, aElementRepresentation_NodeList: StepFEA_HArray1OfNodeRepresentation, aModelRef: StepFEA_FeaModel3d, aElementDescriptor: StepElement_Volume3dElementDescriptor, aMaterial: StepElement_ElementMaterial) -> None: ...
	def Material(self) -> StepElement_ElementMaterial: ...
	def ModelRef(self) -> StepFEA_FeaModel3d: ...
	def SetElementDescriptor(self, ElementDescriptor: StepElement_Volume3dElementDescriptor) -> None: ...
	def SetMaterial(self, Material: StepElement_ElementMaterial) -> None: ...
	def SetModelRef(self, ModelRef: StepFEA_FeaModel3d) -> None: ...

class StepFEA_NodeWithSolutionCoordinateSystem(StepFEA_Node):
	def __init__(self) -> None: ...

class StepFEA_NodeWithVector(StepFEA_Node):
	def __init__(self) -> None: ...
