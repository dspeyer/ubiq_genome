# ubiq_genome

This code is for the first hackathon of [Ubiquitous Genomics](http://ubiquitousgenomics.teamerlich.org/).

To run the first part of the assignment, type

    make final.pdf DIR=/wherever/you/put/the/data/

To run the data through NCBI, type

    python searchmany.py DIR=/wherever/you/put/the/data/

To get the ratios taking into account genome, type

    python infopipeline.py DIR=/wherever/the/matches/folder/is/

To get the ratios not taking into account genome, type

    python infopipeline_2.py DIR=/wherever/the/matches/folder/is/

To pull all the sequences after run through NCBI for each minute, type

    python pulltimes.py DIR=/wherever/you/put/the/data/  DIR=/wherever/the/hasspec/folder/is/

To get the ratios over time taking into account genome, type

    python minrunner.py

To get the ratios over time not taking into account genome, type

    python minrunner_2.py

All code in this repository may be used, modified, and/or redistributed under the terms of the [GNU General Public License, version 2.0](https://www.gnu.org/licenses/old-licenses/gpl-2.0.en.html#SEC1).
