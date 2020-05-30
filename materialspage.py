class materialspage:
    def __init__(self, store):
        self.__sto = store

    def index(self):
        s = '<a href=..>%s</a><a href=addform>%s</a>' % (u'назад', u' добавить')
        s += '<table><th bgcolor=gray></th><th bgcolor=gray>%s</th><th bgcolor=gray>%s</th>' % (
        u'название',u'ценазаграмм')
        r = 1
        bg = ''
        for a in self.__sto.getMaterialCodes():
            s += '<tr%s><td>%d</td>' % (bg, r)
            s += '<td>%s</td>' % self.__sto.getMaterialName(a)
            s += '<td>%s</td>' % self.__sto.getMaterialPriceForGramm(a)
            s += '<td><a href=editform?code=%s>%s</a></td>' % (a, u'редактировать')
            s += '<td><a href=delr?code=%s>%s</a></td></tr>' % (a, u'удалить')
            r += 1
            if bg:
                bg = ''
            else:
                bg = ' bgcolor=silver'
        s += '</table>'
        return s

    index.exposed = True

    def materialform(self, code=0, add=True):
        name,priceForGramm = '',0 
        if add:
            a = 'addaction'
        else:
            a = 'editaction?code=%s' % code
        if code in self.__sto.getMaterialCodes():
            name = self.__sto.getMaterialName(code)
            priceForGramm = self.__sto.getMaterialPriceForGramm(code)
        s = '''<form action=%s method=post>
             <table>
                <tr><td>%s</td><td><input type=text name=name value=%s></td></tr>
                <tr><td>%s</td><td><input type=number name=priceForGramm value=%s></td></tr>
                <tr><td><input type=submit></td><td></td></tr>
            </table>
            </form>''' % (a, u'название', name, u'ценазаграмм', priceForGramm)
        return s

    def addaction(self, name, priceForGramm):
        code = self.__sto.getMaterialNewCode()
        self.__sto.newMaterial(code)
        self.__sto.setMaterialName(code, name)
        self.__sto.setMaterialPriceForGramm(code, priceForGramm)
        return 'материал добавлен<br><a href=index>назад</a>'

    addaction.exposed = True

    def addform(self):
        s = u'Добавить новый материал<br>'
        s += self.materialform(0)
        return s

    addform.exposed = True

    def editform(self, code):
        s = u'Редактировать материал<br>'
        s += self.materialform(int(code), False)
        return s

    editform.exposed = True

    def editaction(self, code, name, priceForGramm):
        self.__sto.setMaterialName(int(code), name)
        self.__sto.setMaterialPriceForGramm(int(code), priceForGramm)
        return 'материал изменён<br><a href=index>назад</a>'

    editaction.exposed = True

    def delr(self, code):
        self.__sto.removeMaterial(int(code))
        return 'материал удалён<br><a href=index>назад</a>'

    delr.exposed = True
