import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def resolver_viga_biapoiada_distribuida(L, q):
    RA = RB = q * L / 2

    x = np.linspace(0, L, 500)
    V = RA - q * x
    M = RA * x - (q * x**2) / 2
    N = np.zeros_like(x)

    fig, axs = plt.subplots(4, 1, figsize=(10, 10),
                            gridspec_kw={'height_ratios': [1, 3, 3, 3]}, sharex=True)

    # --- Viga com carga distribuída (ajustada para sinal de q) ---
    ax_viga = axs[0]
    ax_viga.plot([0, L], [0, 0], color='black', linewidth=4)

    n_setas = 15
    seta_direcao = np.sign(q)
    for xi in np.linspace(0, L, n_setas):
        ax_viga.annotate('', xy=(xi, 0.1 * seta_direcao), xytext=(xi, 0.8 * seta_direcao),
                         arrowprops=dict(facecolor='blue', width=3, headwidth=10))

    ax_viga.text(L / 2, 1.1 * seta_direcao, f'q = {q:.1f} N/m', ha='center', fontsize=11)

    # Apoios
    ax_viga.plot(0, 0, marker='o', markersize=8, color='gray')
    ax_viga.plot(L, 0, marker='^', markersize=10, color='gray')

    ax_viga.set_ylim(-1.5, 1.5)
    ax_viga.axis('off')
    ax_viga.set_title('Viga com carga distribuída uniforme')

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
    axs[3].annotate('Máx: qL²/8', xy=(L/2, q * L**2 / 8),
                   xytext=(L/2 + L/10, q * L**2 / 8 + 20 * np.sign(q)),
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
    st.pyplot(fig)
