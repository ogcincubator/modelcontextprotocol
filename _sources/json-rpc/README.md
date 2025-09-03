# mission-planning-task-model

This BBlock defines the **ontology** and **SHACL shape** for the `mission:PlanningTask` class using PROV-O extensions.

## Purpose

- To define a reusable semantic model for `PlanningTask` activities.
- To provide SHACL shapes to validate RDF data instances of `mission:PlanningTask`.

## Contents

- `shape/planning_task.shape.ttl`: SHACL shape definitions.
- `ontology/mission.ttl`: Ontology terms extending `prov:Activity` to describe mission planning tasks.
- `bblock.json` / `bblock.yaml`: BBlock registration metadata.

## Standards

- Inherits from: [`ogc.ogc-utils.prov`](https://ogcincubator.github.io/bblock-prov-schema/bblock/ogc.ogc-utils.prov)
- Uses: W3C PROV-O vocabulary and SHACL shapes.

## Usage

This BBlock is intended to be referenced by other BBlocks (e.g., `mission-planning-task-prov`) that include provenance traces and examples.

## Validation

Use `pyshacl` to validate RDF data against the shape:

```bash
pyshacl -s shape/planning_task.shape.ttl -d ../mission-planning-task-prov/examples/planning_task.example.ttl -f turtle
