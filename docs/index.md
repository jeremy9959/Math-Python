---
layout: default
title: Syllabus 
nav_order: 1
---

## Python Seminar

Python Seminar, Spring 2024 <br>
University of Connecticut <br>

###  Instructor

- [Jeremy Teitelbaum](https://jeremy9959.net)

### Introduction

This is an informal course on the language python for UConn graduate students in Mathematics.
The goal is to support students in learning aspects of the language that will be useful to them
in the future.  A good knowledge of python is useful for many things ranging from automating routine tasks, to generating
nice graphs, to carrying out experiments in mathematical research.
   

### Schedule

The course meets weekly on Wednesday afternoons from 1:25 PM to 2:15 PM in Monteith 227.

### Assessment

This is an informal course.  There is no assigned homework and there are no exams.
Grading is S/U.  

### Resources

Python is ubiquitous and there are many available resources. There are many resources
on the [Python Beginners Page](https://wiki.python.org/moin/BeginnersGuide/.) Note however that you should install the Anaconda distribution described below rather than using the system python or other installations.

Other references:

1.  *Python Crash Course*, by Eric Matthes.  This is a well-reviewed book that is a reasonably efficient intro to Python.  
It is available free through the [O'Reilly online library via the UConn Library](https://learning.oreilly.com/library/view/python-crash-course/9781098156664/).

1. *Learning Python*, by Mark Lutz.  Published by O'Reilly. 
[Available free  through the O'Reilly online library via the UConn library.](https://learning.oreilly.com/library/view/learning-python-5th/9781449355722/) 
This is a 1600 page comprehensive overview of the Python language. 

2. *The Python Tutorial*, from [python.org](https://docs.python.org/3/tutorial/index.html) If you know some programming in another language you can quickly get a lot from this. 

3. [Complete Python Bootcamp](https://www.udemy.com/course/complete-python-bootcamp/) from Udemy, written by Jose Portilla.  This is an online course.  
You have to pay for it.  It's always on sale and costs between 5 dollars and 20 dollars.  DO NOT pay more. 
If you want a systematic, clearly taught,online course with a thorough coverage of python this is a good choice.

4. [Fluent Python](https://learning.oreilly.com/library/view/fluent-python-2nd/9781492056348/) by Ramalho.  
Also available free from O'Reilly through the UConn library. If you *know* python, this is a beautiful book about how to take full advantage of the
language features.  It also teaches a lot about the language internals. 

5. [Python for Data Analysis (3E)](https://wesmckinney.com/book/).  This is a book that focuses on using Python for data analysis, 
it includes a quick intro to the language generally and
then a detailed discussion of tools for data manipulation and visualization.

In addition, [this page](links.md) includes links to other documents I have created for other courses on a variety of topics.



### Tools

To work with Python you need an implementation of the language on your computer and a tool for working with python files.  
In addition, most of the capabilities of Python come from external library files -- for example, linear algebra is not 
part of the Python language but there is a package called `numpy` that implements algorithms in linear
algebra.  So you need access to these library files.  The key elements are:

1. [The Anaconda Distribution](https://www.anaconda.com)  This includes python, the most commonly used libraries, and a 
tool (a 'package manager') that allows you to download other libraries that you may want for particular purposes.  
This also includes `jupyter` which is a commonly used environment for working with Python. 
*Note that most computers are shipped today with some version of python installed, but you should install Anaconda rather than relying on the preinstalled version of python.*

2. [vscode](https://code.visualstudio.com) This is an "IDE" (integrated development environment). It's like the ultimate text editor. 
It provides a huge collection of tools for writing code and is useful for writing LaTeX and pretty much anything else.

An  alternative to installing software on your computer is to use a cloud resource.  There are a number of these available, but 
the most straightforward is [google colab](http://colab.research.google.com).  You will need a google account to use this.  The advantage
of using this is that we don't have to mess with loading packages and you have easy access to a basic gpu for deep learning applications.
The disadvantage is that you give up a lot of control, you need internet access and you don't have the full suite of capabilities of vscode.

