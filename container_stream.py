import streamlit as st

class Container:
    def __init__(self):
        # Initialize container specifications
        self.length = 20  # feet
        self.width = 8  # feet
        self.height = 8.5  # feet
        self.volume = 1170  # cubic feet (approx.)
        self.payload_capacity = 61700  # lbs
        self.remaining_volume = self.volume  # cubic feet
        self.remaining_payload = self.payload_capacity  # lbs

    def load_goods(self, length, width, height, weight):
        # Calculate the volume of the goods in cubic feet
        goods_volume = length * width * height

        # Check if the goods can fit within the container's remaining volume and payload
        if goods_volume > self.remaining_volume:
            return f"Error: Not enough space. Remaining volume: {self.remaining_volume:.2f} cubic feet."

        if weight > self.remaining_payload:
            return f"Error: Not enough payload capacity. Remaining payload: {self.remaining_payload:.2f} lbs."

        # Deduct the volume and weight of the goods from the container
        self.remaining_volume -= goods_volume
        self.remaining_payload -= weight

        return f"Goods loaded successfully. Remaining volume: {self.remaining_volume:.2f} cubic feet, " \
               f"Remaining payload: {self.remaining_payload:.2f} lbs."


# Streamlit App
def main():
    st.title("20-foot Container Loader")

    # Initialize container
    if "container" not in st.session_state:
        st.session_state.container = Container()

    container = st.session_state.container

    # Input fields for goods dimensions and weight
    with st.form(key="load_form"):
        st.subheader("Enter Goods Dimensions and Weight")
        length = st.number_input("Length (ft):", min_value=0.0, step=0.1)
        width = st.number_input("Width (ft):", min_value=0.0, step=0.1)
        height = st.number_input("Height (ft):", min_value=0.0, step=0.1)
        weight = st.number_input("Weight (lbs):", min_value=0.0, step=1.0)
        submit = st.form_submit_button("Load Goods")

    # Load goods when the form is submitted
    if submit:
        if length > 0 and width > 0 and height > 0 and weight > 0:
            result = container.load_goods(length, width, height, weight)
            if "Error" in result:
                st.error(result)
            else:
                st.success(result)
        else:
            st.error("All dimensions and weight must be greater than zero.")

    # Display remaining container capacity
    st.subheader("Container Status")
    st.write(f"Remaining Volume: {container.remaining_volume:.2f} cubic feet")
    st.write(f"Remaining Payload: {container.remaining_payload:.2f} lbs")


if __name__ == "__main__":
    main()
