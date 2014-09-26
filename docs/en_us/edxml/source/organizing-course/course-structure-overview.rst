###############################
edXML Course Building Blocks
###############################

Before you begin building your edXML course, you should understand the building
blocks of an edX course. See:

* `Courseware`_
* `Supplemental Course Content`_
* `Course Policies`_

###############################
Courseware
###############################

Courseware is the main content of your course, namely lessons and assessments.
The following list describes how courseware is organized in edXML:

* Each course starts with a course outline, which contains one or more
  sections. For more information, see :ref:`The Course Outline XML File`.

* Course sections are at the top level of your course and typically represent a
  time period. In edXML, sections are represented by ``chapter`` elements. For
  more information, see :ref:`Course Chapter XML Files`.

* A section contains one or more subsections. Course subsections are parts of a
  section, and usually represent a topic or other organizing principle. In
  edXML, subsections are represented by ``sequential`` elements. For more
  information, see :ref:`Course Sequential XML Files`.

* A subsection contains one or more units. In edXML, units are represented by
  ``vertical`` elements.  For more information, see :ref:`Course Vertical XML
  Files`.

* Course units are lessons in a subsection that students view as single pages.
  A unit contains one or more components. Course components are objects within
  units that contain your actual course content. For more information, see:

  * :ref:`Course Components`
  * :ref:`Problems and Tools`
  * :ref:`Advanced Components`

###############################
Supplemental Course Content
###############################

In addition to the courseware described above, you course can contain
supplemental content, such as textbooks, custom pages, and files.  The
following list describes the types of supported content:

* Course about pages appear in the course list for prospective students and are
  used to market your course. For more information, see :ref:`The Course About
  Pages`.

* Course assets are any supplemental files you use in your course, such as a
  syllabus as a PDF file or an image that appears in an HTML component. For
  more information, see :ref:`Course Assets`.

* Course pages are custom pages that you can have appear in the top navigation
  menu of your course.  For more information, see :ref:`Course Pages`.

###############################
Course Policies
###############################

Course policies determine how your course functions. For example, policies
control grading and content experiments. For more information, see
:ref:`Policies`.