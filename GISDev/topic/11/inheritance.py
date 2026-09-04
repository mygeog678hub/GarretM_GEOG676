class Molecule:
    def __init__(self, name = 'Generic'):
        self.name = name
        self.atomlist = []
    def addAtom(self, atom):
        self.atomlist.append(atom)
    def __repr__(self):
        str = 'This is a molecule named %s\n' %self.name
        str = str + 'It has %d atoms\n' %len(self.atomlist)
        for atom in self.atomlist:
            str = str + 'atom' + '\n'
        return str

class Better_Molecule(Molecule):
    def __init__(self, name = 'Generic', basis = '6-31G**'):
        self.basis = basis
        Molecule.__init__(self, name) # Calls the constructor for the parent function
    def addBasis(self):
        self.basis = []
        for atom in self.atomlist:
            self.basis.append(atom)

newMolecule = Better_Molecule('dihydrogen monoxide', '5-18Q**')
newMolecule.addAtom('H') # Object uses method defined in Molecule instead of Better_Molecule
newMolecule.addBasis() # Object can also use methods of Better_Molecule