/*
Copyright 2008-2020 Thomas Paviot (tpaviot@gmail.com)

This file is part of pythonOCC.
pythonOCC is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

pythonOCC is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU Lesser General Public License for more details.

You should have received a copy of the GNU Lesser General Public License
along with pythonOCC.  If not, see <http://www.gnu.org/licenses/>.
*/
%define BINTOBJDRIVERSDOCSTRING
"BinTObjDrivers module, see official documentation at
https://www.opencascade.com/doc/occt-7.4.0/refman/html/package_bintobjdrivers.html"
%enddef
%module (package="OCC.Core", docstring=BINTOBJDRIVERSDOCSTRING) BinTObjDrivers


%{
#ifdef WNT
#pragma warning(disable : 4716)
#endif
%}

%include ../common/CommonIncludes.i
%include ../common/ExceptionCatcher.i
%include ../common/FunctionTransformers.i
%include ../common/Operators.i
%include ../common/OccHandle.i


%{
#include<BinTObjDrivers_module.hxx>

//Dependencies
#include<Standard_module.hxx>
#include<NCollection_module.hxx>
#include<BinMDF_module.hxx>
#include<Message_module.hxx>
#include<TDocStd_module.hxx>
#include<BinLDrivers_module.hxx>
#include<TDF_module.hxx>
#include<BinObjMgt_module.hxx>
#include<Resource_module.hxx>
#include<PCDM_module.hxx>
#include<LDOM_module.hxx>
#include<CDF_module.hxx>
#include<TDF_module.hxx>
#include<TColgp_module.hxx>
#include<TColStd_module.hxx>
#include<TCollection_module.hxx>
#include<Storage_module.hxx>
%};
%import Standard.i
%import NCollection.i
%import BinMDF.i
%import Message.i
%import TDocStd.i
%import BinLDrivers.i
%import TDF.i
%import BinObjMgt.i

%pythoncode {
from OCC.Core.Exception import *
};

/* public enums */
/* end public enums declaration */

/* python proy classes for enums */
%pythoncode {
};
/* end python proxy for enums */

/* handles */
%wrap_handle(BinTObjDrivers_DocumentRetrievalDriver)
%wrap_handle(BinTObjDrivers_DocumentStorageDriver)
%wrap_handle(BinTObjDrivers_IntSparseArrayDriver)
%wrap_handle(BinTObjDrivers_ModelDriver)
%wrap_handle(BinTObjDrivers_ObjectDriver)
%wrap_handle(BinTObjDrivers_ReferenceDriver)
%wrap_handle(BinTObjDrivers_XYZDriver)
/* end handles declaration */

/* templates */
/* end templates declaration */

/* typedefs */
/* end typedefs declaration */

/***********************
* class BinTObjDrivers *
***********************/
%rename(bintobjdrivers) BinTObjDrivers;
class BinTObjDrivers {
	public:
		/****************** AddDrivers ******************/
		%feature("compactdefaultargs") AddDrivers;
		%feature("autodoc", "No available documentation.

Parameters
----------
aDriverTable: BinMDF_ADriverTable
aMsgDrv: Message_Messenger

Returns
-------
None
") AddDrivers;
		static void AddDrivers(const opencascade::handle<BinMDF_ADriverTable> & aDriverTable, const opencascade::handle<Message_Messenger> & aMsgDrv);

		/****************** DefineFormat ******************/
		%feature("compactdefaultargs") DefineFormat;
		%feature("autodoc", "Defines format 'tobjbin' and registers its read and write drivers in the specified application.

Parameters
----------
theApp: TDocStd_Application

Returns
-------
None
") DefineFormat;
		static void DefineFormat(const opencascade::handle<TDocStd_Application> & theApp);

		/****************** Factory ******************/
		%feature("compactdefaultargs") Factory;
		%feature("autodoc", "No available documentation.

Parameters
----------
aGUID: Standard_GUID

Returns
-------
opencascade::handle<Standard_Transient>
") Factory;
		static const opencascade::handle<Standard_Transient> & Factory(const Standard_GUID & aGUID);

};


%extend BinTObjDrivers {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************************
* class BinTObjDrivers_DocumentRetrievalDriver *
***********************************************/
class BinTObjDrivers_DocumentRetrievalDriver : public BinLDrivers_DocumentRetrievalDriver {
	public:
		/****************** BinTObjDrivers_DocumentRetrievalDriver ******************/
		%feature("compactdefaultargs") BinTObjDrivers_DocumentRetrievalDriver;
		%feature("autodoc", "No available documentation.

Returns
-------
None
") BinTObjDrivers_DocumentRetrievalDriver;
		 BinTObjDrivers_DocumentRetrievalDriver();

		/****************** AttributeDrivers ******************/
		%feature("compactdefaultargs") AttributeDrivers;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMsgDriver: Message_Messenger

Returns
-------
opencascade::handle<BinMDF_ADriverTable>
") AttributeDrivers;
		virtual opencascade::handle<BinMDF_ADriverTable> AttributeDrivers(const opencascade::handle<Message_Messenger> & theMsgDriver);

};


%make_alias(BinTObjDrivers_DocumentRetrievalDriver)

%extend BinTObjDrivers_DocumentRetrievalDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*********************************************
* class BinTObjDrivers_DocumentStorageDriver *
*********************************************/
class BinTObjDrivers_DocumentStorageDriver : public BinLDrivers_DocumentStorageDriver {
	public:
		/****************** BinTObjDrivers_DocumentStorageDriver ******************/
		%feature("compactdefaultargs") BinTObjDrivers_DocumentStorageDriver;
		%feature("autodoc", "No available documentation.

Returns
-------
None
") BinTObjDrivers_DocumentStorageDriver;
		 BinTObjDrivers_DocumentStorageDriver();

		/****************** AttributeDrivers ******************/
		%feature("compactdefaultargs") AttributeDrivers;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMsgDriver: Message_Messenger

Returns
-------
opencascade::handle<BinMDF_ADriverTable>
") AttributeDrivers;
		virtual opencascade::handle<BinMDF_ADriverTable> AttributeDrivers(const opencascade::handle<Message_Messenger> & theMsgDriver);

};


%make_alias(BinTObjDrivers_DocumentStorageDriver)

%extend BinTObjDrivers_DocumentStorageDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/********************************************
* class BinTObjDrivers_IntSparseArrayDriver *
********************************************/
class BinTObjDrivers_IntSparseArrayDriver : public BinMDF_ADriver {
	public:
		/****************** BinTObjDrivers_IntSparseArrayDriver ******************/
		%feature("compactdefaultargs") BinTObjDrivers_IntSparseArrayDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") BinTObjDrivers_IntSparseArrayDriver;
		 BinTObjDrivers_IntSparseArrayDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
theSource: BinObjMgt_Persistent
theTarget: TDF_Attribute
theRelocTable: BinObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const BinObjMgt_Persistent & theSource, const opencascade::handle<TDF_Attribute> & theTarget, BinObjMgt_RRelocationTable & theRelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
theSource: TDF_Attribute
theTarget: BinObjMgt_Persistent
theRelocTable: BinObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & theSource, BinObjMgt_Persistent & theTarget, BinObjMgt_SRelocationTable & theRelocTable);

};


%make_alias(BinTObjDrivers_IntSparseArrayDriver)

%extend BinTObjDrivers_IntSparseArrayDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***********************************
* class BinTObjDrivers_ModelDriver *
***********************************/
class BinTObjDrivers_ModelDriver : public BinMDF_ADriver {
	public:
		/****************** BinTObjDrivers_ModelDriver ******************/
		%feature("compactdefaultargs") BinTObjDrivers_ModelDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") BinTObjDrivers_ModelDriver;
		 BinTObjDrivers_ModelDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: BinObjMgt_Persistent
Target: TDF_Attribute
RelocTable: BinObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const BinObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, BinObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: BinObjMgt_Persistent
RelocTable: BinObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, BinObjMgt_Persistent & Target, BinObjMgt_SRelocationTable & RelocTable);

};


%make_alias(BinTObjDrivers_ModelDriver)

%extend BinTObjDrivers_ModelDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/************************************
* class BinTObjDrivers_ObjectDriver *
************************************/
class BinTObjDrivers_ObjectDriver : public BinMDF_ADriver {
	public:
		/****************** BinTObjDrivers_ObjectDriver ******************/
		%feature("compactdefaultargs") BinTObjDrivers_ObjectDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") BinTObjDrivers_ObjectDriver;
		 BinTObjDrivers_ObjectDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: BinObjMgt_Persistent
Target: TDF_Attribute
RelocTable: BinObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const BinObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, BinObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: BinObjMgt_Persistent
RelocTable: BinObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, BinObjMgt_Persistent & Target, BinObjMgt_SRelocationTable & RelocTable);

};


%make_alias(BinTObjDrivers_ObjectDriver)

%extend BinTObjDrivers_ObjectDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/***************************************
* class BinTObjDrivers_ReferenceDriver *
***************************************/
class BinTObjDrivers_ReferenceDriver : public BinMDF_ADriver {
	public:
		/****************** BinTObjDrivers_ReferenceDriver ******************/
		%feature("compactdefaultargs") BinTObjDrivers_ReferenceDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") BinTObjDrivers_ReferenceDriver;
		 BinTObjDrivers_ReferenceDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: BinObjMgt_Persistent
Target: TDF_Attribute
RelocTable: BinObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const BinObjMgt_Persistent & Source, const opencascade::handle<TDF_Attribute> & Target, BinObjMgt_RRelocationTable & RelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
Source: TDF_Attribute
Target: BinObjMgt_Persistent
RelocTable: BinObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & Source, BinObjMgt_Persistent & Target, BinObjMgt_SRelocationTable & RelocTable);

};


%make_alias(BinTObjDrivers_ReferenceDriver)

%extend BinTObjDrivers_ReferenceDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/*********************************
* class BinTObjDrivers_XYZDriver *
*********************************/
class BinTObjDrivers_XYZDriver : public BinMDF_ADriver {
	public:
		/****************** BinTObjDrivers_XYZDriver ******************/
		%feature("compactdefaultargs") BinTObjDrivers_XYZDriver;
		%feature("autodoc", "No available documentation.

Parameters
----------
theMessageDriver: Message_Messenger

Returns
-------
None
") BinTObjDrivers_XYZDriver;
		 BinTObjDrivers_XYZDriver(const opencascade::handle<Message_Messenger> & theMessageDriver);

		/****************** NewEmpty ******************/
		%feature("compactdefaultargs") NewEmpty;
		%feature("autodoc", "No available documentation.

Returns
-------
opencascade::handle<TDF_Attribute>
") NewEmpty;
		opencascade::handle<TDF_Attribute> NewEmpty();

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
theSource: BinObjMgt_Persistent
theTarget: TDF_Attribute
theRelocTable: BinObjMgt_RRelocationTable

Returns
-------
bool
") Paste;
		Standard_Boolean Paste(const BinObjMgt_Persistent & theSource, const opencascade::handle<TDF_Attribute> & theTarget, BinObjMgt_RRelocationTable & theRelocTable);

		/****************** Paste ******************/
		%feature("compactdefaultargs") Paste;
		%feature("autodoc", "No available documentation.

Parameters
----------
theSource: TDF_Attribute
theTarget: BinObjMgt_Persistent
theRelocTable: BinObjMgt_SRelocationTable

Returns
-------
None
") Paste;
		void Paste(const opencascade::handle<TDF_Attribute> & theSource, BinObjMgt_Persistent & theTarget, BinObjMgt_SRelocationTable & theRelocTable);

};


%make_alias(BinTObjDrivers_XYZDriver)

%extend BinTObjDrivers_XYZDriver {
	%pythoncode {
	__repr__ = _dumps_object
	}
};

/* harray1 classes */
/* harray2 classes */
/* hsequence classes */
