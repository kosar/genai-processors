# GenAI Processors: A Practitioner's Guide

This guide provides a practical introduction to the GenAI Processors library, focusing on how to use it to build powerful and flexible AI pipelines.

## Core Concepts

The GenAI Processors library is built around a few core concepts:

*   **`Processor`**: A `Processor` is the fundamental building block of the library. It represents a unit of work that takes a stream of `ProcessorPart`s as input and produces a stream of `ProcessorPart`s as output. Processors can be chained together to create complex data processing pipelines.

*   **`ProcessorPart`**: A `ProcessorPart` is a wrapper around a piece of content, such as text, an image, or audio. It also contains metadata about the content, such as its MIME type and role.

*   **Streams**: The library uses asynchronous streams to pass data between processors. This allows for efficient, non-blocking I/O and enables the creation of real-time applications.

## Getting Started

To start using the GenAI Processors library, you'll first need to install it:

```bash
pip install genai-processors
```

Once the library is installed, you can start creating processors and building pipelines.

## Creating a Simple Processor

The easiest way to create a processor is to use the `@processor` decorator. This decorator can be applied to any async function that takes an `AsyncIterable[ProcessorPart]` as input and returns an `AsyncIterable[ProcessorPartTypes]`.

Here's an example of a simple processor that converts all text to uppercase:

```python
from genai_processors import processor
from genai_processors.content_api import ProcessorPart
from typing import AsyncIterable

@processor
async def uppercase_processor(
    content: AsyncIterable[ProcessorPart],
) -> AsyncIterable[ProcessorPart]:
    async for part in content:
        if part.text:
            yield ProcessorPart(text=part.text.upper())
```

## Chaining Processors

Processors can be chained together using the `+` operator. This creates a new processor that applies each processor in the chain in sequence.

Here's an example of how to chain the `uppercase_processor` with a processor that adds a prefix to the text:

```python
@processor
async def prefix_processor(
    content: AsyncIterable[ProcessorPart],
) -> AsyncIterable[ProcessorPart]:
    async for part in content:
        if part.text:
            yield ProcessorPart(text=f"Processed: {part.text}")

# Chain the processors together
chained_processor = uppercase_processor + prefix_processor
```

## Parallelizing Processors

Processors can be parallelized using the `//` operator. This creates a new processor that applies each processor in parallel to the input stream and merges the output streams.

## Built-in Processors

The GenAI Processors library comes with a number of built-in processors that you can use in your applications. These include:

*   **`GenaiModel`**: A processor for making calls to the Gemini API.
*   **`LiveProcessor`**: A processor for real-time, streaming interactions with the Gemini API.
*   **`PartProcessor`**: A base class for creating processors that operate on individual `ProcessorPart`s.

## Conclusion

The GenAI Processors library provides a powerful and flexible way to build AI pipelines. By understanding the core concepts of `Processor`, `ProcessorPart`, and streams, you can create sophisticated applications that are both efficient and easy to maintain.
