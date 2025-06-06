# casos/viga_biapoiada_concentrada.py
import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def resolver_viga_biapoiada(L, P):
    a = L / 2  # posição da carga no meio

    # Reações nos apoios (simétrico)
    RA = RB = P / 2

    x = np.linspace(0, L, 500)

    V = np.piecewise(x, [x < a, x >= a], [lambda x: RA, lambda x: RA - P])
    M = np.piecewise(x, [x < a, x >= a], [lambda x: RA * x, lambda x: RA * x - P * (x - a)])
    N = np.zeros_like(x)

    fig, axs = plt.subplots(4, 1, figsize=(10, 10), gridspec_kw={'height_ratios': [1, 3, 3, 3]}, sharex=True)

    # --- Viga com carga ---
    ax_viga = axs[0]
    ax_viga.plot([0, L], [0, 0], color='black', linewidth=4)
    ax_viga.annotate('', xy=(a, -1), xytext=(a, -0.1),
                 arrowprops=dict(facecolor='blue', width=7, headwidth=20, headlength=15))
    ax_viga.text(a, -1.3, f'P = {P:.1f} N', ha='center', fontsize=11)


    # Apoios: simples (círculo) e duplo (triângulo)
    ax_viga.plot(0, 0, marker='o', markersize=8, color='gray')
    ax_viga.plot(L, 0, marker='^', markersize=10, color='gray')

    ax_viga.set_ylim(-2, 2)
    ax_viga.axis('off')
    ax_viga.set_title('Representação da Viga com Carga Concentrada no Meio')

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
    axs[3].annotate('Máx: PL/4', xy=(a, RA * a), xytext=(a + 0.5, RA * a + 20),
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
