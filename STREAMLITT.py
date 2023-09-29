import pandas as pd
import streamlit as st
import plotly.express as px
import datetime


def main():
    st.set_page_config(
        page_title="Offre d'emploi",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded",
    )


    

    # Add custom menu items as links
    st.sidebar.markdown("📧 [Obtenir l'aide / Signaler un bug](mailto:anaslachhab42@gmail.com)")
    

if __name__ == "__main__":
    main()

st.title("Trouvez votre Future ⭐⭐⭐")
st.subheader("Votre Avenir Professionnel 👔")

job = pd.read_csv('jobs-Finalyyy.csv')


# Display current date and row count on the same line
current_date = "2023/09/29"
filtered_rows_count = len(job)
st.markdown(f'<div style="display: flex; justify-content: space-between;">'
            f"<div>📋 Nombre d'Emploi: {filtered_rows_count}</div>"
            f'<div>📅 Dernière Mise a Jour: {current_date}</div>'
            f'</div>', unsafe_allow_html=True)

st.sidebar.header("⛏️ Filtrage:")

# Sidebar filters
location = st.sidebar.multiselect('location: 🏠', options=sorted(job['location'].unique()))
salaire = st.sidebar.multiselect('salaire: 💰', options=sorted(job['salaire'].unique()))
etude = st.sidebar.multiselect('etude: 🎓', options=sorted(job['etude'].unique()))
contrat = st.sidebar.multiselect('contrat: 📝', options=sorted(job['contrat'].unique()))
domaine = st.sidebar.multiselect('domaine: 🛠️', options=sorted(job['domaine'].unique()))

# Apply filters only if selections are not empty
if location or salaire or etude or contrat or domaine:
    filtered_data = job.copy()

    # Apply location filter
    if location:
        filtered_data = filtered_data[filtered_data['location'].isin(location)]

    # Apply salaire filter
    if salaire:
        filtered_data = filtered_data[filtered_data['salaire'].isin(salaire)]

    # Apply etude filter
    if etude:
        filtered_data = filtered_data[filtered_data['etude'].isin(etude)]

    # Apply contrat filter
    if contrat:
        filtered_data = filtered_data[filtered_data['contrat'].isin(contrat)]

    # Apply domaine filter
    if domaine:
        filtered_data = filtered_data[filtered_data['domaine'].isin(domaine)]

    if not filtered_data.empty:
        # Calculate title counts for filtered data
        title_counts_filtered = filtered_data['titles'].value_counts()
        title_counts_filteredss = title_counts_filtered.head(20).sort_values(ascending =True)
        top_titles = title_counts_filtered.head(100).index
        
        
        # Create a horizontal bar chart using Plotly for filtered data
        fig_filtered = px.bar(
           
            title_counts_filteredss, orientation='h', 
            labels={'index': 'Titre', 'value': 'Nombre'},
            title="Top 20 offre d'emploi 💼"
        )
        st.plotly_chart(fig_filtered)


        # Use the selected title to filter data for the pie charts
        selected_title = st.selectbox('🖱️ Sélectionnez un titre:', top_titles)


        
        # Pie chart for selected étude
        experience_counts = filtered_data[filtered_data['titles'] == selected_title]['experience'].value_counts()
        fig_pie_exper = px.pie(
            values=experience_counts, names=experience_counts.index,
            title=f"Types d'experiences 👷 pour {selected_title}"
        )
        st.plotly_chart(fig_pie_exper)
        

        # Pie chart for selected étude
        etude_counts = filtered_data[filtered_data['titles'] == selected_title]['etude'].value_counts()
        fig_pie_etude = px.pie(
            values=etude_counts, names=etude_counts.index,
            title=f"Types des niveaux d'etude 🎓 pour {selected_title}"
        )
        st.plotly_chart(fig_pie_etude)
         

        # Pie chart for selected étude
        salaire_counts = filtered_data[filtered_data['titles'] == selected_title]['salaire'].value_counts()
        fig_pie_salaire = px.pie(
            values=salaire_counts, names=salaire_counts.index,
            title=f"Types des salaires 💰 pour {selected_title} "
        )
        st.plotly_chart(fig_pie_salaire)
        
        

        # Pie chart for selected étude
        contrat_counts = filtered_data[filtered_data['titles'] == selected_title]['contrat'].value_counts()
        fig_pie_contrat = px.pie(
            values=contrat_counts, names=contrat_counts.index,
            title=f"Type des contrat 📝 pour {selected_title}"
        )
        st.plotly_chart(fig_pie_contrat)


    else:
        st.write('Aucun résultat.😔')
else:
    st.write("")
    st.write('⭐ Veuillez sélectionner au moins une option de filtrage.')

st.sidebar.markdown('## 🌐 Liens:')
st.sidebar.markdown('📧 [Gmail](mailto:anaslachhab666@gmail.com)')
st.sidebar.markdown('🔗 [Github](https://github.com/anas6666)')
st.sidebar.markdown('🔗 [Linkedin](https://www.linkedin.com/in/anas-lachhab-6131471b1/)')



st.write("")
st.write("")
st.write("")
st.write("")
st.markdown("### Introduction:")
st.write("Bonjour à tous,")
st.write("Aujourd'hui, je vous présente une nouvelle solution qui va révolutionner la façon dont vous cherchez des opportunités professionnelles au Maroc. cette web application conçue pour vous fournir une analyse complète des offres d'emploi provenant de \"MAROC ANNONCE\". Nous comprenons à quel point il peut être difficile de trouver les opportunités qui correspondent à vos compétences et à vos aspirations. C'est pourquoi nous avons créé cette application pour vous aider à naviguer à travers les différentes offres et vous fournir des informations clés pour prendre des décisions éclairées.❤️‍🔥")
