## Installation

Run the following to install:

```python
pip install buser-xml-to-dict
```  

## Usage

```python

CTE_XML = '/'.join([os.path.dirname(__file__), 'pathtofile.xml'])
cte = XmlAdapter.from_xmlpath(CTE_XML)
cte['cteProc__CTe__infCte__ide__cUF']
```