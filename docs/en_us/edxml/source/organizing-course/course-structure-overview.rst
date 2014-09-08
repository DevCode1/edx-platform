###############################
edXML Course Building Blocks
###############################

Before you begin building your edXML course, you should understand the building
blocks of an edX course.

* Each course starts with a course outline, which contains one or more
  sections. See :ref:`The Course Outline XML File`.

* Course sections are at the top level of your course and typically represent a
  time period. In edXML, sections are represented by ``chapter`` elements. See
  :ref:`Course Chapter XML Files`.

* A section contains one or more subsections. Course subsections are parts of a
  section, and usually represent a topic or other organizing principle. In
  edXML, subsections are represented by ``sequential`` elements. See
  :ref:`Course Sequential XML Files`.

* A subsection contains one or more units. In edXML, units are represented by
  ``vertical`` elements.  See :ref:`Course Vertical XML Files`.

* Course units are lessons in a subsection that students view as single pages.
  A unit contains one or more components. Course components are objects within
  units that contain your actual course content. See:

  * :ref:`Course Components`
  * :ref:`Problems and Tools`
  * :ref:`Advanced Components`