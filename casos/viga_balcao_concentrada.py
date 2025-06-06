# casos/viga_balcao_concentrada.py
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def resolver_viga_balcao(L, P):
    x = np.linspace(0, L, 500)

    # Esforços internos
    N = np.zeros_like(x)               
    V = np.full_like(x, P)            
    M = P * (x - L)                   

    fig, axs = plt.subplots(4, 1, figsize=(10, 10),
                            gridspec_kw={'height_ratios': [1, 3, 3, 3]}, sharex=True)

    # --- Desenho da viga com carga ---
    ax_viga = axs[0]
    ax_viga.plot([0, L], [0, 0], color='black', linewidth=4)
    seta_altura = 1.0 * np.sign(-P)
    texto_altura = 1.3 * np.sign(-P)
    ax_viga.annotate('', xy=(L, seta_altura), xytext=(L, 0.1 * np.sign(-P)),
                     arrowprops=dict(facecolor='blue', width=7, headwidth=20, headlength=15))
    ax_viga.text(L, texto_altura, f'P = {P:.1f} N', ha='center', va='center', fontsize=11)
    for offset in np.linspace(-0.4, 0.4, 5):
        ax_viga.plot([0 + offset, 0 + offset], [-0.2, 0.2], color='gray', linewidth=1)
    ax_viga.set_ylim(-2, 2)
    ax_viga.axis('off')
    ax_viga.set_title('Representação da Viga com Carga Concentrada')

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
    axs[2].text(L / 2, V[0] * 0.6, sinal, ha='center', fontsize=16, weight='bold')
    axs[2].set_title('Diagrama de Esforço Cortante (V)')
    axs[2].axhline(0, color='gray', linewidth=0.8)
    axs[2].legend()
    axs[2].grid(True)

    # --- Diagrama M ---
    axs[3].fill_between(x, 0, M, where=(M >= 0), color='green', alpha=0.3)
    axs[3].fill_between(x, 0, M, where=(M < 0), color='red', alpha=0.3)
    axs[3].plot(x, M, label='M(x)', color='black')
    axs[3].set_title('Diagrama de Momento Fletor (M)')
    axs[3].annotate('Máx: -PL', xy=(0, M[0]), xytext=(1, M[0] - 100*np.sign(M[0])),
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
