# KG Parts Library

This is the KG Genetic Parts library. It is written with basic yaml for data portability purposes.

## Purpose

The KG Genetic Parts Library is a complete genetic parts library, covering all major organisms, with consistent and high-quality documentation. 

## Rules
1. All genes must have a unique name, including genes used between different toolkits
2. Parts should be accessible from a URL. No weird special characters.
3. A sequence should only have 1 name.
4. All references must also exist in the papers directory
5. In cases of proteins encoded for a certain organism, add a parathesis tag to the end of the protein. For example, `SceI(Scerevisae)`.
6. In cases of proteins designed to have a C terminal tag, append a (c) to the front of the protein. For example, `(c)GFP(Ecoli)`.
