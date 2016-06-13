with open("Dictionary.txt","r") as f:
        words = f.readlines()
        words = [x.strip('\n') for x in words]


   
symbols = """
Ac,Al,Am,Sb,Ar,As,At,Ba,Bk,Be,Bi,Bh,B,Br,Cd,Ca,Cf,C,Ce,Cs,Cl,Cr,
Co,Cu,Cm,Ds,Db,Dy,Es,Er,Eu,Fm,F,Fr,Gd,Ga,Ge,Au,Hf,Hs,He,Ho,H,In,I,
Ir,Fe,Kr,La,Lr,Pb,Li,Lu,Mg,Mn,Mt,Md,Hg,Mo,Nd,Ne,Np,Ni,Nb,N,No,Os,
O,Pd,P,Pt,Pu,Po,K,Pr,Pm,Pa,Ra,Rn,Re,Rh,Rb,Ru,Rf,Sm,Sc,Sg,Se,Si,Ag,
Na,Sr,S,Ta,Tc,Te,Tb,Tl,Th,Tm,Sn,Ti,W,Uub,Uuh,Uuo,Uup,Uuq,Uus,Uut,
Uuu,U,V,Xe,Yb,Y,Zn,Zr
"""
#source: http://www.lenntech.com/periodic/name/alphabetic.htm

symlist = symbols.split(',')
symlist = [s.strip() for s in symlist]
symlist = [s.strip('\n') for s in symlist]

##print("Trying word:",words[123])
##if words[123] == "wrwes":
##    print("YES!")
##else:
##    print("Funnily enough, no")
