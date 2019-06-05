from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    """ this is a docstring, so that readthedocs will find something 
       
===== 
Title 
===== 
Subtitle 
-------- 
Titles are underlined (or over- 
and underlined) with a printing 
nonalphanumeric 7-bit ASCII 
character. Recommended choices 
are "``= - ` : ' " ~ ^ _ * + # < >``". 
The underline/overline must be at 
least as long as the title text. 

A lone top-level (sub)section 
is lifted up to be the document's 
(sub)title.

- This is item 1 
- This is item 2

:Authors: 
    Tony J. (Tibs) Ibbs, 
    David Goodger
    (and sundry other good-natured folks)

:Version: 1.0 of 2001/08/08 
:Dedication: To cookie monster    
    """
    return "Hello World!"
