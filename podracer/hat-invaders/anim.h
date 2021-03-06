// Animation data for Trinket/Gemma + LED matrix backpack jewelry.
// Edit this file to change the animation; it's unlikely you'll need
// to edit the source code.
 
static const uint8_t anim[] = {

  // Animation bitmaps.  Each frame of animation MUST contain
  // 8 lines of graphics data (there is no error checking for
  // length).  Each line should be prefixed with the letter 'B',
  // followed by exactly 8 binary digits (0 or 1), no more,
  // no less (again, no error checking).  '0' represents an
  // 'off' pixel, '1' an 'on' pixel.  End line with a comma.
  0b00011000, // This is the first frame for alien #1
  0b00111100, // If you squint you can kind of see the
  0b01111110, // image in the 0's and 1's.
  0b11011011,
  0b11111111,
  0b00100100,
  0b01011010,
  0b10100101,
  // The 9th line (required) is the time to display this frame,
  // in 1/100ths of a second (e.g. 100 = 1 sec, 25 = 1/4 sec,
  // etc.).  Range is 0 (no delay) to 255 (2.55 seconds).  If
  // longer delays are needed, make duplicate frames.
  25, // 0.25 seconds
 
  0b00011000, // This is the second frame for alien #1
  0b00111100,
  0b01111110,
  0b11011011,
  0b11111111,
  0b00100100,
  0b01011010,
  0b01000010,
  25, // 0.25 second delay
 
  // Frames 3 & 4 for alien #1 are duplicates of frames 1 & 2.
  // Rather than list them 'the tall way' again, the lines are merged here...
  0b00011000, 0b00111100, 0b01111110, 0b11011011, 0b11111111, 0b00100100, 0b01011010, 0b10100101, 25,
  0b00011000, 0b00111100, 0b01111110, 0b11011011, 0b11111111, 0b00100100, 0b01011010, 0b01000010, 25
};
