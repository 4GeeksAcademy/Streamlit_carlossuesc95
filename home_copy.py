import streamlit as st

def main():
    st.set_page_config(page_title="Bienvenid@ al portal predictivo XYZ", page_icon="🤖", layout="centered")

    st.title("Bienvenid@ al portal predictivo de la empresa XYZ")
    st.write("**Por favor seleccione el servicio predictivo que desea utilizar**")

    opcion = st.radio(
        "Seleccione el servicio:",
        ("Predicción del tipo de flor", "Predicción de imagen"),
        index=None
    )

    st.markdown("---")

    if opcion == "Predicción del tipo de flor":
        way_to_pred = st.radio(
            "¿Cómo desea realizar la predicción de la flor?",
            ("Ingresando datos manualmente", "Subiendo un archivo CSV"),
            index=None
        )

        st.markdown("### Ir a la página")

        if way_to_pred == "Ingresando datos manualmente":
            st.page_link("pages/pred_iris_man.py", label="➡️ Predicción Iris (manual)", icon="🌸")
        elif way_to_pred == "Subiendo un archivo CSV":
            st.page_link("pages/pred_iris_csv.py", label="➡️ Predicción Iris (CSV)", icon="📄")

    elif opcion == "Predicción de imagen":
        st.markdown("### Ir a la página")
        st.page_link("pages/pred_imagen.py", label="➡️ Predicción de imagen", icon="🖼️")

    else:
        st.info("Selecciona una opción para ver los accesos.")

if __name__ == "__main__":
    main()