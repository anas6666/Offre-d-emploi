import pandas as pd
import streamlit as st
import plotly.express as px

# Load your data here (replace 'jobs-Finalyyy.csv' with your actual CSV file)
job = pd.read_csv('jobs-Finalyyy.csv')

def main():
    st.set_page_config(
        page_title="Offre d'emploi",
        page_icon="💼",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    st.title("Trouvez votre Future ⭐⭐⭐")
    st.subheader("Votre Avenir Professionnelll 👔")
    
    # Display current date and row count...
    current_date = "2023/08/24"
    filtered_rows_count = len(job)
    st.markdown(f'<div style="display: flex; justify-content: space-between;">'
                f"<div>📋 Nombre d'emploi: {filtered_rows_count}</div>"
                f'<div>📅 Dernière mise a jour: {current_date}</div>'
                f'</div>', unsafe_allow_html=True)
    
    st.sidebar.header("⛏️ Filtrage:")
    
    # Sidebar filters...
    location = st.sidebar.multiselect('location: 🏠', options=sorted(job['location'].unique()))
    salaire = st.sidebar.multiselect('salaire: 💰', options=sorted(job['salaire'].unique()))
    etude = st.sidebar.multiselect('etude: 🎓', options=sorted(job['etude'].unique()))
    contrat = st.sidebar.multiselect('contrat: 📝', options=sorted(job['contrat'].unique()))
    domaine = st.sidebar.multiselect('domaine: 🛠️', options=sorted(job['domaine'].unique()))
    
    if st.width <= 800:
        comments_section()

    # Apply filters only if selections are not empty
    if location or salaire or etude or contrat or domaine:
        filtered_data = job.copy()

        # Apply location filter...
        if location:
            filtered_data = filtered_data[filtered_data['location'].isin(location)]

        # Apply salaire filter...
        if salaire:
            filtered_data = filtered_data[filtered_data['salaire'].isin(salaire)]

        # Apply etude filter...
        if etude:
            filtered_data = filtered_data[filtered_data['etude'].isin(etude)]

        # Apply contrat filter...
        if contrat:
            filtered_data = filtered_data[filtered_data['contrat'].isin(contrat)]

        # Apply domaine filter...
        if domaine:
            filtered_data = filtered_data[filtered_data['domaine'].isin(domaine)]

        if not filtered_data.empty:
            # Calculate title counts for filtered data...
            title_counts_filtered = filtered_data['titles'].value_counts()
            title_counts_filteredss = title_counts_filtered.head(20).sort_values(ascending=True)
            top_titles = title_counts_filtered.head(100).index

            # Create a horizontal bar chart using Plotly for filtered data...
            fig_filtered = px.bar(
                title_counts_filteredss, orientation='h',
                labels={'index': 'Titre', 'value': 'Nombre'},
                title="Top 20 offre d'emploi 💼"
            )
            st.plotly_chart(fig_filtered)

            # Use the selected title to filter data for the pie charts...
            selected_title = st.selectbox('🖱️ Sélectionnez un titre:', top_titles)

            # Pie chart for selected étude...
            experience_counts = filtered_data[filtered_data['titles'] == selected_title]['experience'].value_counts()
            fig_pie_exper = px.pie(
                values=experience_counts, names=experience_counts.index,
                title=f"Types d'experiences 👷 pour {selected_title}"
            )
            st.plotly_chart(fig_pie_exper)

            # Pie chart for selected étude...
            etude_counts = filtered_data[filtered_data['titles'] == selected_title]['etude'].value_counts()
            fig_pie_etude = px.pie(
                values=etude_counts, names=etude_counts.index,
                title=f"Types des niveaux d'etude 🎓 pour {selected_title}"
            )
            st.plotly_chart(fig_pie_etude)

            # Pie chart for selected salaire...
            salaire_counts = filtered_data[filtered_data['titles'] == selected_title]['salaire'].value_counts()
            fig_pie_salaire = px.pie(
                values=salaire_counts, names=salaire_counts.index,
                title=f"Types des salaires 💰 pour {selected_title} "
            )
            st.plotly_chart(fig_pie_salaire)

            # Pie chart for selected contrat...
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

if __name__ == "__main__":
    main()


