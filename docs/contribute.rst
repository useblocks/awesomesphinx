Contribute
==========

Updating package data
---------------------

Changing existing data
~~~~~~~~~~~~~~~~~~~~~~
To extend or manipulate the data for a specific extension or theme, please
add an entry to the file ``/docs/additions.rst``.

We use the `needextend <https://sphinx-needs.readthedocs.io/en/latest/directives/needextend.html>`_ 
mechanism of `Sphinx-Needs <https://sphinx-needs.com>`_ to add,
change or replace values of imported elements.

.. code-block:: rst

    .. needextend:: SUNPY-SPHINX-THEME
       :sphinx_type: theme
       :+tags: theme, sunpy 

The above code is changing data of a need-element with the ID ``SUNPY-SPHINX-THEME``.
It overwrites the ``sphinx_type`` with the value ``theme`` and 
also extends the ``tags`` attribute by a new value.

Changing or better extending data is a common task in the awesomesphinx projects.
It's mostly used to classify an extension or theme, to put it in specific categories for the user.


Adding new package
~~~~~~~~~~~~~~~~~~
Normally all extensions and themes get imported automatically from PiPy if they have set the correct
classifiers in their packages.

However, there are projects, which are not released on PYPI or haven't set the right classifiers. 
Therefore these packages need to be registered in awesomesphinx by hand.


Register a package from PYPI
++++++++++++++++++++++++++++

Updating classifiers
********************
The best and most correct way of documenting a package here is to make sure it contains the 
correct classifiers. If this is the case, it will be found on the upcoming import run.

Each Python packaging tool does support setting classifiers. Please take a look at the related documentation to do so.

The used classifiers for filtering are defined inside ``/projects.py`` file and are currently:

.. literalinclude:: /../projects.py
   :lines: 6-11


Not matching classifiers
************************
If a package does not match the classifiers, which are used to search for packages on PyPi, it can be added
by hand. However, it still must be available on PyPi!

Please open the file ``/projects.py`` and add the package-name to 
the ``EXTRA_PROJECTS`` list.

.. code-block:: python

   EXTRA_PROJECTS = [
    'MY-NEW-PACKAGE'  # <-- This is new
    'sphinx-copybutton',
    'doxysphinx'
   ] 

Please be sure that the used name can be used to identify the package on PyPi, for instance by copying 
the name from the PyPi URL of the package.

Manually add a new package
++++++++++++++++++++++++++
Please open the related category file from the ``/docs/categories`` folder.

After the ``needimport`` statement you are free to add a new Sphinx-Needs element, which represents
the package.

.. code-block:: rst

    .. software:: My new theme
       :id: MY-NEW-theme
       :sphinx_type: theme
       :monthly: 0
       :release_date: 2022-09-24T21:26:03
       :release_name: 2.1.0
       :code: https://github.com/me/package
       :pypi: https://pypi.org/package
       :website: https://my-new-package.com

The values for ``points`` and ``release_days`` get calculated automatically.

.. warning:: 

   Please be aware that this is the **worst** way of adding a new extension/theme.

   The values of ``release_date`` and ``monthly`` are not accurate and would need to be 
   maintained by hand. It is much better to release the package on PyPi with the correct
   classifiers. 

Developing docs
---------------

Run scripts
~~~~~~~~~~~
The ``pypi_json.py`` script is using Google BigQuery to get information about the download numbers of PyPi.
You need a google cloud account and an **authentication-file** to run these queries. 

The installation guide of `pypinfo <https://github.com/ofek/pypinfo/blob/master/README.rst#installation>`_ has a great 
chapter on how to get and configure a google cloud account.

The **authentication-file** must be set via ENV variable.
If you use our ``.vscode/launch.json`` config, this is set automatically to 
``"GOOGLE_APPLICATION_CREDENTIALS": "${workspaceFolder}/secrets/google_cloud.json"``

Technical background
~~~~~~~~~~~~~~~~~~~~

The AwesomeSphinx data workflow is as follows:

1. ``/scripts/pypi_json.py`` gets executed

   1. Search for packages on PyPi by classifiers
   2. Requests package info from PyPi for each package
   3. Queries PyPi-BigQuery-data for download numbers of the last 30 days
   4. Stores all data in a ``pypi_data.json`` files

2. ``/scripts/needs_json.py`` gets executed

   1. Loads ``pypi_data.json``
   2. Extracts needed data only
   3. Constructs need-objects internally
   4. Creates an ``awesome.json``, which contains the need-objects and is compliant with the Sphinx-Needs ``needs.json`` format.


3. Sphinx build gets started

   1. ``needimport`` for ``awesome.json`` is used to import need-object for specific categories 
   2. Jinja templates get rendered and inject data
   3. Value calculation is done via the ``dynamic functions`` feature of Sphinx-Needs


Own Awesome X list
------------------
The used code and documentation configuration are not specific to Sphinx.

With 1-2 line changes in the file ``/projects.py`` for the used classifiers filters, documentation projects can 
be created for other Python-based projects.

It must be currently Python-based, as the ``pypi_json.py`` script is using PyPi and BigQuery Table from PyPi to get needed data.
If this gets changed as well, also other tools can be documented as well.



