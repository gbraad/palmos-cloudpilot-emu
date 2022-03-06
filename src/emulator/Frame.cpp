#include "Frame.h"

Frame::Frame(size_t bufferSize)
    : buffer(make_unique<uint8[]>(bufferSize)), bufferSize(bufferSize) {}

uint8* Frame::GetBuffer() { return buffer.get(); }

size_t Frame::GetBufferSize() const { return bufferSize; }

uint8 Frame::GetBpp() const { return bpp; }

uint32 Frame::GetLineWidth() const { return lineWidth; }

uint32 Frame::GetLines() const { return lines; }

uint8 Frame::GetMargin() const { return margin; }

uint32 Frame::GetBytesPerLine() const { return bytesPerLine; }

uint32 Frame::GetFirstDirtyLine() const { return firstDirtyLine; }

uint32 Frame::GetLastDirtyLine() const { return lastDirtyLine; }

bool Frame::GetHasChanges() const { return hasChanges; }

uint8 Frame::GetScaleX() const { return scaleX; }

uint8 Frame::GetScaleY() const { return scaleY; }
