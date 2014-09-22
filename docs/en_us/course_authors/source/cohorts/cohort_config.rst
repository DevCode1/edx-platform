.. _Enabling and Configuring Cohorts:

############################################
Enabling and Configuring the Cohort Feature
############################################

To support private discussions for cohorts of students, you select a strategy
for assigning your students to cohort groups: automated assignment, manual
assignment, or a hybrid approach. See :ref:`Options for Assigning Students to
Cohorts`. You also decide whether to open any of the course-wide discussion
topics to participation by all students. 

After you select a strategy, you complete these steps (as applicable):

#. :ref:`Enable the cohort feature<Enable Cohorts>`.

#. Based on the strategy you select for assigning students to cohort groups:
   
  * :ref:`Enable automated cohort assignment<Enable Automated Cohort
    Assignment>` and
    :ref:`define the auto cohort groups<Define Auto Cohort Groups>`.

  * :ref:`Define manual cohort groups<Define the Manual Cohort Groups>` and
    :ref:`assign students to them<Assign Students to Cohort Groups Manually>`.

  * Do both. 

3. :ref:`Identify the course-wide discussion topics<Identifying Private
   CourseWide Discussion Topics>` that you want to support private, cohort-only
   participation. This procedure is optional.

You complete these procedures in Studio and on the Instructor Dashboard. For an
optimal student experience, configuration of the cohort feature should be as
complete as possible prior to the start date of your course.

.. _Enable Cohorts:

********************************
Enabling the Cohort Feature
********************************

#. Open the course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. In the **Cohort Configuration** field, place your cursor between the
   supplied pair of braces.

#. Type ``"cohorted": true``. 

#. Click **Save Changes**. Studio reformats the name:value pair you just
   entered to indent it on a new line.
   
 .. image:: ../Images/Enable_cohorts.png
  :alt: Cohort Configuration dictionary field with the cohorted key defined 
        as true

.. _Implementing the Automated Assignment Strategy:

***************************************************
Implementing the Automated Assignment Strategy
***************************************************

To implement automated assignment of students to cohort groups you add two more
values to the **Cohort Configuration** advanced setting field.

You complete these procedures if you are using either the automated or hybrid
assignment strategy for your course. For more information, see :ref:`All
Automated Assignment` or :ref:`Hybrid Assignment`.

.. _Enable Automated Cohort Assignment:

============================================
Enable Automated Cohort Assignment
============================================

#. Open the course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. In the **Cohort Configuration** field, place your cursor after
   ``"cohorted": true``.

#. Type a comma ``,`` character and then press Enter.

#. Type ``"auto_cohort": true``. 

#. Click **Save Changes**. Studio resequences and reformats the name:value
   pairs.

 .. image:: ../Images/Enable_auto_cohorts.png
  :alt: Cohort Configuration dictionary field with the auto_cohort key defined 
        as true

You continue by defining the auto cohort groups. 

.. _Define Auto Cohort Groups:

============================================
Define the Auto Cohort Groups
============================================

.. note:: Students can see the name of the cohort group they are assigned to. 
 The message "This post is visible only to Group *cohort name*" appears with
 each post in discussion topics that support private, cohort-only
 participation.

#. Open the course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. In the **Cohort Configuration** field, place your cursor after
   ``"auto_cohort": true,`` and then press Enter.

#. For a fully automated assignment strategy, you define a set of groups. Place
   each group name within quotation marks, separate the names with commas, and
   place each one on a new line:
   
 .. code:: 

   "auto_cohort_groups": [
       "example_1st_group_name",
       "example_2nd_group_name",
       "example_3rd_group_name"
   ],

.. here to alow indented formatting of next line only

  For a hybrid strategy, you only define a single group. Type
   ``"auto_cohort_groups": ["example_group_name"]`` and then press Enter again.

5. Click **Save Changes**. Studio resequences and reformats your entry.

 .. image:: ../Images/Multiple_auto_cohort_groups.png
  :alt: Cohort Configuration dictionary field with the auto_cohort_groups key 
        with one value

.. spacer line

 .. image:: ../Images/Single_auto_cohort_group.png
  :alt: Cohort Configuration dictionary field with the auto_cohort_groups key 
        with one value

When students who are not already assigned to a cohort group visit the
**Discussion** page, they are randomly assigned to an auto cohort group.

.. _Implementing the Manual Assignment Strategy:

***************************************************
Implementing the Manual Assignment Strategy
***************************************************

To implement manual assignment of students to cohort groups, you define the
manual cohort groups and then assign students to them. You complete these
procedures if you are using either the manual or hybrid assignment strategy for
your course. For more information, see :ref:`All Manual Assignment` or
:ref:`Hybrid Assignment`.

You must :ref:`enable the cohort feature<Enable Cohorts>` for your course
before you can complete these procedures.

.. _Define the Manual Cohort Groups:

==========================================
Define the Manual Cohort Groups
==========================================

.. note:: Students can see the name of the cohort group they are assigned to. 
 The message "This post is visible only to Group *cohort name*" appears with
 each post in discussion topics that support private, cohort-only
 participation.

#. In your live course, select the **Instructor** page. 

#. On the **Membership** page, scroll to the **Cohort Group Management**
   section at the bottom.

#. Click **Add Cohort Group**.

#. Supply a name for the group, and then click **Add Cohort Group** below the
   **Cohort Name** field.

.. question to Brian about same label on two different buttons

.. _Assign Students to Cohort Groups Manually:

==========================================
Assign Students to Cohort Groups Manually
==========================================

#. In your live course, select the **Instructor** page. 

#. On the **Membership** page, scroll to the **Cohort Group Management**
   section at the bottom.

#. Select the cohort group that you want to add students to from the drop down
   list.

.. something here about what happens if you select an auto cohort group? does anything happen? maybe just reassurance that nothing in particular happens?  

4. In the **Add Students** field, enter the username or email address of a
   single student, or enter multiple names or addresses separated by commas or
   new lines. You can copy data from a CSV file of email addresses and paste it
   into this field.

 .. note:: Verify that email addresses are accurate after you enter them. 
    You do not receive notification for any messages that bounce.
 
5. Click **Add Students**.
   
   The students are assigned to the selected manual cohort group. A message
   appears to indicate the number of students who were added to the cohort
   group. Because students can belong to only one cohort group, the message
   also indicates the number of students whose assignment to another cohort
   group was changed by this procedure.

.. _Identifying Private CourseWide Discussion Topics:

*****************************************************************
Identifying Private Course-Wide Discussion Topics
*****************************************************************

You can configure one or more of the course-wide discussion topics in your
course to support private interactions among the members of the cohort groups. 

.. note:: Content-specific discussion topics in course units only
 support private participation among cohort members. Content-specific
 discussion topics cannot be changed from private to open.

For more information about content-specific and course-wide discussion topics,
see :ref:`Organizing_discussions`.

.. _Configure CourseWide Discussion Topics as Private:

======================================================
Configure Course-Wide Discussion Topics as Private
======================================================

Before you set up course-wide discussion topics to support private
conversations for the cohort groups, you add the topics in Studio. See
:ref:`Create CourseWide Discussion Topics`.

To configure a course-wide discussion topic as supporting private, cohort-
specific interchanges:

#. Open the course in Studio. 

#. Select **Settings**, then **Advanced Settings**.

#. In the **Cohort Configuration** field, place your cursor after
   ``"cohorted":true`` and then press Enter.

#. To specify a single discussion topic, type ``"cohorted_discussions":
   ["example_topic_name"]`` and then press Enter again.
   
   To specify two or more discussion topics, you place each topic name within
   quotation marks, separate the names with commas, and place each one on a new
   line:
 
  .. code::

   "cohorted_discussions": [
       "example_1st_topic_name",
       "example_2nd_topic_name",
       "example_3rd_topic_name"
   ]   
   
5. Click **Save Changes**. Studio resequences and reformats your entry.

 .. image:: ../Images/Configure_cohort_topic.png
  :alt: Cohort Configuration dictionary field with the cohorted_discussions key
        defined as true
