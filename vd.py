import matplotlib.pyplot as plt
import matplotlib.patches as patches

def create_hickory_venn_diagram():

    fig, ax = plt.subplots(figsize=(10, 10))
    
    fig.patch.set_facecolor('#E6E6E6')
    ax.set_facecolor('#E6E6E6')

    circle_settings = [
        {'center': (0.35, 0.6), 'radius': 0.35},  # Top Left
        {'center': (0.65, 0.6), 'radius': 0.35},  # Top Right
        {'center': (0.5, 0.35), 'radius': 0.35}   # Bottom
    ]

    for circle in circle_settings:
        c = patches.Circle(
            circle['center'], 
            circle['radius'], 
            linewidth=6, 
            edgecolor='black', 
            facecolor='none'
        )
        ax.add_patch(c)
    
    text_elements = [
        # Top Left (Straight lines)
        (0.22, 0.68, 'V', 'black', 35),
        (0.18, 0.58, 'W', 'black', 35),
        (0.27, 0.53, 'X', 'blue', 35), 
        (0.25, 0.77, 'I', 'black', 35),

        # Top Right (Curved lines)
        (0.78, 0.72, 'O', 'black', 35),
        (0.82, 0.63, 'U', 'black', 35),
        (0.73, 0.58, 'C', 'black', 35),
        (0.75, 0.78, 'S', 'black', 35),

        # Bottom (Greek Lowercase)
        (0.52, 0.08, 'μ', 'black', 40),
        (0.42, 0.12, 'η', 'black', 40),
        (0.58, 0.18, 'ζ', 'black', 40),
        (0.48, 0.22, 'σ', 'green', 40), 

        # Top Intersection (Mixed Straight/Curved)
        (0.52, 0.73, 'R', 'black', 35),
        (0.48, 0.63, 'B', 'red', 35),   
        (0.51, 0.56, 'J', 'black', 35),

        # Left Intersection (Greek Straight)
        (0.32, 0.42, 'Γ', 'black', 40), 
        (0.37, 0.30, 'Π', 'black', 40), 
        (0.28, 0.33, 'Ψ', 'black', 40), 

        # Right Intersection (Greek Curved)
        (0.68, 0.43, 'φ', 'black', 40), 
        (0.63, 0.30, 'ω', 'black', 40), 
        (0.77, 0.37, 'ϵ', 'black', 40), 

        # Center (Target)
        (0.50, 0.45, '?', 'black', 45)  
    ]

    for x, y, char, color, size in text_elements:
        ax.text(
            x, y, char, 
            color=color, 
            fontsize=size, 
            ha='center', 
            va='center', 
            fontfamily='serif', 
            fontweight='bold'
        )

    # 4. Final Formatting
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)
    ax.set_aspect('equal')
    ax.axis('off') 

    # 5. Save/Show
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    create_hickory_venn_diagram()
