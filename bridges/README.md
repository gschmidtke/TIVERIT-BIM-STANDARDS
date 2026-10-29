# Interoperability Plane

The `bridges/` tree contains governed mappings from canonical TIVERIT requirements into external machine-readable standards and exchange formats.

## Authority boundary

Bridge artifacts are projections. They do not become alternate normative sources. If an external representation cannot express the full meaning of a TIVERIT requirement, the mapping must record that limitation explicitly.

## Initial bridge families

```text
bridges/
  ids/     buildingSMART Information Delivery Specification mappings
  bsdd/    buildingSMART Data Dictionary mappings
  ifc/     IFC entity/property/classification mappings
```

Directories are created when their first governed mapping is added; empty placeholder artifacts are not required.

## IDS bridge rule

IDS 1.0 is intended for computer-interpretable IFC information requirements such as entities, properties, classifications, materials, relations, quantities, and values. It is not a general-purpose carrier for geometry or application-internal identity semantics.

Therefore an IDS bridge must state whether the source requirement is fully representable, partially representable, or not representable. A generated `.ids` file must not silently omit TIVERIT semantics that IDS cannot carry.

The first pilot maps the S8 governed shared-parameter consistency requirement. Property presence/name/value constraints may later be projected into IDS when a governed IFC property-set mapping exists. Revit shared-parameter GUID authority is retained as TIVERIT/Revit governance and is not assumed to be directly expressible in IDS.
