list_mark = []
class Mark():
    def __init__(self,sid,cid,mark,credits):
        self._sid = sid
        self._cid = cid
        self._mark = mark
        self._credits = credits
    def add_mark(self):#method to add a mark object to list_mark
        ob_mark = Mark(self._sid, self._cid, self._mark,self._credits)
        list_mark.append(ob_mark)