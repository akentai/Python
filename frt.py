def fruits(category = [], category_images=[]):

    category.extend( ["Μήλο", "Πορτοκάλι", "Μπανάνα", "Μανταρίνι", "Φράουλα", "Πεπόνι", "Καρπούζι", "Ρόδι"] )
    category_images.extend( ["fruits/apple.jpg", "fruits/orange.jpg", "fruits/banana.jpg", \
                       "fruits/madarin.jpg", "fruits/strawberry.jpg", "fruits/melon.jpg", \
                       "fruits/watermelon.jpg", "fruits/rodi.jpg"] )
 
    return


def sports(category = [], category_images=[]):

    category.extend( ["Μπάσκετ", "Ποδόσφαιρο", "Γυμναστική", "Καράτε", "Τέννις"] )
    category_images.extend( ["sports/Basketball.jpg", "sports/Football.jpg", "sports/Gymnastics.jpg", "sports/Karate.jpg", "sports/Tennis.jpg"] )
    
    return


def seasons(category = [], category_images=[]):

    category.extend( ["Φθινόπωρο", "Χειμώνας", "Άνοιξη", "Καλοκαίρι", \
                "Φθινόπωρο", "Χειμώνας", "Άνοιξη", "Καλοκαίρι", \
                "Χειμώνας", "Άνοιξη", "Καλοκαίρι"] )
    category_images.extend(["seasons/Autumn1.jpg", "seasons/Winter1.jpg", "seasons/Spring1.jpg", "seasons/Summer1.jpg", \
               "seasons/Autumn2.jpg", "seasons/Winter2.jpg", "seasons/Spring2.jpg", "seasons/Summer2.jpg", \
               "seasons/Winter3.jpg", "seasons/Spring3.jpg", "seasons/Summer3.jpg"] )
    
    return
