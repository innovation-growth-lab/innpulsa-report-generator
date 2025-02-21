# Markdown Guide - Quick Reference

## Table of Contents
- [Headers](#headers)
- [Emphasis](#emphasis)
- [Lists](#lists)
- [Links](#links)
- [Images](#images)
- [Code](#code)
- [Tables](#tables)
- [Blockquotes](#blockquotes)
- [Horizontal Rules](#horizontal-rules)
- [Line Breaks](#line-breaks)
- [Task Lists](#task-lists)
- [Footnotes](#footnotes)
- [Escaping Characters](#escaping-characters)

## Headers
# H1 Header
## H2 Header
### H3 Header
#### H4 Header
##### H5 Header
###### H6 Header

Alternative H1 Header
===================

Alternative H2 Header
-------------------

## Emphasis
*Italic text* or _italic text_
**Bold text** or __bold text__
***Bold and italic*** or ___bold and italic___
~~Strikethrough text~~

## Lists
### Unordered Lists
- Item 1
* Item 2
+ Item 3
  - Nested item
    * Deeper nested item

### Ordered Lists
1. First item
2. Second item
3. Third item
   1. Nested ordered item
   2. Another nested item

## Links
[Basic link](https://www.example.com)
[Link with title](https://www.example.com "Link title")
<https://www.example.com> <!-- Direct URL -->
[Reference link][reference]
[Reference link 2][reference]

[reference]: https://www.example.com

## Images
![Alt text](assets/igl_logo.png)
![Alt text](assets/innpulsa_logo.png "Image title")
![Alt text](assets/zasca_logo.png "Image title")

## Code
### Inline Code
Use `inline code` within text

### Code Blocks
```
python
def hello_world():
print("Hello, World!")
``` 


## Tables
| Header 1 | Header 2 | Header 3 |
|----------|----------|----------|
| Cell 1   | Cell 2   | Cell 3   |
| Cell 4   | Cell 5   | Cell 6   |

### Alignment in Tables
| Left | Center | Right |
|:-----|:------:|------:|
|Left  |Center  |Right  |

## Blockquotes
> Single line blockquote
>
> Multiple line
> blockquote
>> Nested blockquote

## Horizontal Rules
Three or more hyphens, asterisks, or underscores:

---
***
___

## Line Breaks
End a line with two spaces  
to create a line break

Or use a blank line

to create a paragraph break

## Task Lists
- [x] Completed task
- [ ] Incomplete task
  - [x] Nested completed task
  - [ ] Nested incomplete task

## Footnotes
Here's a sentence with a footnote[^1].

[^1]: This is the footnote content.

## Escaping Characters
\* Asterisk  
\\ Backslash  
\` Backtick  
\{ \} Curly braces  
\[ \] Square brackets  
\( \) Parentheses  
\# Hash symbol  
\+ Plus sign  
\- Minus sign (hyphen)  
\. Period  
\! Exclamation mark  
\| Pipe

## Additional Tips
### Definition Lists
Term
: Definition

### Highlighting
==Highlighted text==

### Subscript and Superscript
H~2~O (subscript)
X^2^ (superscript)

### Emoji
:smile: :heart: :thumbsup:

---
**Note**: Not all markdown processors support all these elements. Some features might require extensions or specific markdown flavors.