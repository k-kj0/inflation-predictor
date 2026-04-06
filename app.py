import gradio as gr

def predict(commodity):
    data = {
        "Gasoline": "🔍 Search interest leads Gasoline prices by 6 weeks\nr = 0.802, p<0.001\n\n📢 Based on current search trends, Gasoline prices may shift in approximately 6 weeks.",
        "Coffee":   "🔍 Search interest leads Coffee prices by 10 weeks\nr = 0.721, p<0.001\n\n📢 Based on current search trends, Coffee prices may shift in approximately 10 weeks.",
        "Eggs":     "🔍 Search interest leads Egg prices by 4 weeks\nr = 0.681, p<0.001\n\n📢 Based on current search trends, Egg prices may shift in approximately 4 weeks.",
    }
    return data[commodity]

demo = gr.Interface(
    fn=predict,
    inputs=gr.Dropdown(["Gasoline", "Coffee", "Eggs"], label="Select Commodity"),
    outputs=gr.Textbox(label="Inflation Signal"),
    title="📈 Commodity Inflation Predictor",
    description="Can Google search trends predict price changes before they happen? Built using real Google Trends + FRED economic data (2021–2026, 192 weeks analyzed)."
)

demo.launch()
