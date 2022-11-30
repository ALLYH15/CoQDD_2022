# Import des librairies et package

import streamlit as st

import os

from PIL import Image



st.set_option('deprecation.showPyplotGlobalUse', False)

 

# ======== Lien Streamlit ========

#streamlit run "C:\Users\aly.traore\Documents\STREAMLIT_PROJET_OPA\QDD_Streamlit.py"


# ======= Organisation Sommaire/Sidebar/etc ========

st.sidebar.title("Sommaire")

pages=['Comité de QDD',
       'Introduction',
       'Approche opérationnelle de la QDD',
       'Cartographie des flux de données', 
       'Tableau de bord',
       'Suivi du contrôle de la QDD',
       'Retard et le fichier de synthèse des contrôles',
       'Contrôles faits',
       "Evolution du tableau de bord",
       "Merci pour votre attention"]

page = st.sidebar.radio("Aller vers",pages)


if page == pages[0]:
    
  
   img1 = Image.open("Diapositive1.PNG")
   st.image(img1, caption='Image Source: Audiens', width=None, use_column_width=None, clamp=False, channels='RGB', output_format='auto')

   
   txt = st.text('Présenté par Aly TRAORE')


elif page == pages[1]:
    
   st.subheader("1. Introduction")
   
   img3 = Image.open("Diapositive3.PNG")
   st.image(img3)



elif page == pages[2]:
    
   st.subheader('2. L’approche opérationnelle de la QDD')
   
   st.write("Une bonne approche opérationnelle de la QDD passe par les étapes suivantes :")
   
   
   img4 = Image.open("Diapositive4.PNG")
   st.image(img4)
   
   #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
    
elif page == pages[3]:
    
    st.subheader('3. La cartographie des flux de données')
    
    
    model = st.radio( "Quelle type de cartographie pour des flux de données ? ",
                   ('Cycle de vie de la donnée','Description des flux'))
   
    if model=='Cycle de vie de la donnée':
        
        #st.write("Flux des données Partie 1")
        
        st.write("Cartographier les flux de données offre à l’organisme une vision à 360°de la masse des données depuis la collecte jusqu’à l’utilisation finale.")
    
       
        img5 = Image.open("Diapositive5.PNG")
        st.image(img5) 
        
        #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
   
    else : 
        #st.write("Description des flux")
        
        st.write("La cartographie des flux présente les données entrantes, sortantes et cibles dans les process.")
      
        
        img6 = Image.open("Diapositive6.PNG")
        st.image(img6)
      
        #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
        
elif page == pages[4]:     
    
    st.subheader('4. Le tableau de bord')
    
   
    model = st.radio( "Quel modele de tableau de bord à mettre en place ? ",
                     ('Objectif du tableau de bord', 'Composition du tableau de bord'))
    
    if model=='Objectif du tableau de bord':
       #st.write("Tableau de bord 1")
       
       st.write("Il permet d’attester de l’activité de pilotage et de suivi des données au sein de la structure.")
    
       
       img7 = Image.open("Diapositive7.PNG")
       st.image(img7) 
       
       #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
   
    else : 
         st.write("Le tableau de bord permet d’attester de l’activité de pilotage et de suivi des données au sein de la structure.")
         st.write("Il rappelle pour chaque contrôle")
      
        
         img8 = Image.open("Diapositive8.PNG")
         st.image(img8)
         
         #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
    
elif page == pages[5]:     
    
    st.subheader('5. Le suivi du contrôle de la QDD')
    
    st.write("Nombre de contrôle réalisé en fonction de la période définie")

    img9 = Image.open("Diapositive9.PNG")
    st.image(img9) 
       
    #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
   
  
    
elif page == pages[6]:     
    
    st.subheader('6. Le retard et le fichier de synthèse des contrôles')
    
    st.write("la procedure de stockage du fichier de synthèse")
     
    
    img10 = Image.open("Diapositive10.PNG")
    st.image(img10)
    
    #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
    
elif page == pages[7]:     
    
    st.subheader('7. Les contrôles faits')
    
    st.write("Les contrôles effectués pour l'année 2022")
     
       
    img11 = Image.open("Diapositive11.PNG")
    st.image(img11) 
       
    #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
   
    
elif page == pages[8]:     
    
    st.subheader("8. l'evolution du tableau de bord")
    
    st.write("Lors de la mise à jour de la Politique de la QDD, nous avons évoqué des nouveaux contrôles qui devront être mis en place en 2023.")
     
    
    img12 = Image.open("Diapositive12.PNG")
    st.image(img12)   
    
    #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')
    
   
elif page == pages[9]:
    
     st.subheader('9. Merci pour votre attention')
        
       
        
     #txt = st.text_area('Vos remarques et suggestions sur la partie operationelle de la QDD :')    


     img13 = Image.open("Diapositive13.PNG")
     st.image(img13)   
     
     
