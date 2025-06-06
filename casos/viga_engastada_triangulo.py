# casos/viga_engastada_triangulo.py
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def resolver_viga_engastada_triangulo(L, q0):
    x = np.linspace(0, L, 500)
    qx = q0 * x / L

    # Reações no engaste
    Rv = q0 * L / 2
    Ma = q0 * L**2 / 3

    # Esforço cortante e momento
    V = Rv - (q0 * x**2) / (2 * L)
    M = Rv * x - (q0 * x**3) / (6 * L)
    N = np.zeros_like(x)

    fig, axs = plt.subplots(4, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [1, 3, 3, 3]}, sharex=True)

    # --- Viga com carga triangular ---
    ax_viga = axs[0]
    ax_viga.plot([0, L], [0, 0], color='black', linewidth=4)
    n_setas = 20
    for xi in np.linspace(0, L, n_setas):
        altura = q0 * xi / L
        ax_viga.annotate('', xy=(xi, 0.1), xytext=(xi, 0.1 + altura / 50),
                         arrowprops=dict(facecolor='blue', width=2, headwidth=8))
    ax_viga.text(L / 2, 0.5, f'Triangular: q₀ = {q0:.1f} N/m', ha='center', fontsize=11)
    for offset in np.linspace(-0.4, 0.4, 5):
        ax_viga.plot([0 + offset, 0 + offset], [-0.2, 0.2], color='gray', linewidth=1)

    ax_viga.set_ylim(-1.5, 1.5)
    ax_viga.axis('off')
    ax_viga.set_title('Viga engastada com carga triangular crescente')

    # --- Diagrama N ---
    axs[1].fill_between(x, 0, N, where=(N >= 0), color='green', alpha=0.3)
    axs[1].fill_between(x, 0, N, where=(N < 0), color='red', alpha=0.3)
    axs[1].plot(x, N, label='N(x)', color='black')
    axs[1].set_title('Diagrama de Esforço Normal (N)')
    axs[1].axhline(0, color='gray', linewidth=0.8)
    axs[1].legend()
    axs[1].grid(True)

    # --- Diagrama V ---
    axs[2].fill_between(x, 0, V, color='orange', alpha=0.4)
    axs[2].plot(x, V, label='V(x)', color='black')
    sinal = '+' if V[0] > 0 else '-' if V[0] < 0 else '0'
    axs[2].text(L / 2, V[int(len(x)/2)] * 0.6, sinal, ha='center', fontsize=16, weight='bold')
    axs[2].set_title('Diagrama de Esforço Cortante (V)')
    axs[2].axhline(0, color='gray', linewidth=0.8)
    axs[2].legend()
    axs[2].grid(True)

    # --- Diagrama M ---
    axs[3].fill_between(x, 0, M, where=(M >= 0), color='green', alpha=0.3)
    axs[3].fill_between(x, 0, M, where=(M < 0), color='red', alpha=0.3)
    axs[3].plot(x, M, label='M(x)', color='black')
    axs[3].set_title('Diagrama de Momento Fletor (M)')
    axs[3].annotate('Máx: q₀·L²/3', xy=(0, Ma),
                   xytext=(L * 0.2, Ma + 0.1 * Ma),
                   arrowprops=dict(facecolor='red', shrink=0.05), fontsize=10)
    axs[3].axhline(0, color='gray', linewidth=0.8)
    axs[3].legend()
    axs[3].grid(True)

    for ax in axs[1:]:
        ax.set_ylabel("Valor")
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)

    axs[3].set_xlabel("Posição x (m)")
    plt.tight_layout()
    plt.tight_layout()
    st.pyplot(fig) 
