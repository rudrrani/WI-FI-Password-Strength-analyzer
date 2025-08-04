import matplotlib.pyplot as plt
import streamlit as st

def show_strength_chart_streamlit(entropy):
    labels = ['Weak', 'Moderate', 'Strong']
    values = [0, 0, 0]

    # Assign the correct value based on entropy
    if entropy < 30:
        values[0] = entropy
    elif entropy < 50:
        values[1] = entropy
    else:
        values[2] = entropy

    # Define improved bar colors with softer shades
    colors = ['#ff4d4d', '#ffb84d', '#5cd65c']

    fig, ax = plt.subplots(figsize=(5, 3.5))  # smaller for mobile


    bars = ax.bar(labels, values, color=colors, edgecolor='black', linewidth=1.2)

    # Add text labels on top of bars
    for bar in bars:
        height = bar.get_height()
        if height > 0:
            ax.text(bar.get_x() + bar.get_width()/2, height + 1, f"{height}", 
                    ha='center', va='bottom', fontsize=12, fontweight='bold')

    ax.set_title("📊 Wi-Fi Password Strength", fontsize=16, fontweight='bold')
    ax.set_ylabel("Entropy Score", fontsize=12)
    ax.set_ylim(0, 100)
    ax.grid(axis='y', linestyle='--', alpha=0.6)

    # Improve spacing and remove extra borders
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)

    st.pyplot(fig, use_container_width=True)

