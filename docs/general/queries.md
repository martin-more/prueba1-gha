---
title: Queries
---

# Queries

By default all the fields the API exposes are nested under a root Query type.

This creates a schema where the root type Query has one single field called
name.

As you notice we don't provide a way to fetch data. In order to do so we need to
provide a `resolver`, a function that knows how to fetch data for a specific
field.

For example in this case we could have a function that always returns the same
name:

