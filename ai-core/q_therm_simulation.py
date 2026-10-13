"""
Project: Q-THERM (Quantum Quartz Metamaterials for Passive Radiative Cooling)
Module: ai-core / q_therm_simulation.py
Description: Python simulation script for phonon resonance frequencies in nanostructured 
             Silicon Dioxide (SiO2) lattices targeting the atmospheric infrared window (8-13 um).
"""

import numpy as np

class QThermSimModel:
    def __init__(self, crystal_type="Alpha-Quartz", purity_pct=99.99):
        self.crystal_type = crystal_type
        self.purity_pct = purity_pct
        # Fereastra atmosferică optimă pentru răcire radiativă (în micrometri - um)
        self.atmospheric_window_min = 8.0  
        self.atmospheric_window_max = 13.0 

    def calculate_phonon_resonance(self, lattice_constant_nm: float) -> float:
        """
        Simulează frecvența de rezonanță fononică în funcție de constanta rețelei nanostructurate.
        Valoare orientativă bazată pe proprietățile cuarțului pur (SiO2).
        """
        base_frequency_thz = 30.0 # Valoare de referință pentru legăturile Si-O
        # Corecție cuantică bazată pe scalarea nanometrică
        scaling_factor = 5.0 / lattice_constant_nm
        resonance_thz = base_frequency_thz * scaling_factor
        return round(resonance_thz, 4)

    def evaluate_radiative_cooling_efficiency(self, emission_wavelength_um: float) -> dict:
        """
        Verifică dacă lungimea de undă emisă se încadrează în fereastra atmosferică 
        pentru a asigura expulzarea energiei termice direct în vidul cosmic (Sky Cooling).
        """
        in_window = self.atmospheric_window_min <= emission_wavelength_um <= self.atmospheric_window_max
        
        status = "OPTIMAL: Direct Space Radiation (No Greenhouse Absorption)" if in_window else \
                 "SUB-OPTIMAL: Absorption by Atmospheric Gases"
                 
        return {
            "wavelength_um": emission_wavelength_um,
            "in_atmospheric_window": in_window,
            "status": status
        }

    def run_simulation_pipeline(self):
        print(f"=== Q-THERM QUANTUM SIMULATION PIPELINE ===")
        print(f"Material: {self.crystal_type} (Purity: {self.purity_pct}%)")
        
        # Testare pe diferite dimensiuni de rețea nanostructurată
        test_spacings = [3.5, 4.2, 5.0] # nanometri
        
        results = []
        for spacing in test_spacings:
            freq = self.calculate_phonon_resonance(spacing)
            # Calcul lungime de undă asociata (lambda = c / f)
            wavelength = round(300 / freq, 2) # aproximare simplificată pentru simulare
            eval_res = self.evaluate_radiative_cooling_efficiency(wavelength)
            
            results.append({
                "lattice_spacing_nm": spacing,
                "frequency_thz": freq,
                "wavelength_um": wavelength,
                "evaluation": eval_res["status"]
            })
            
        return results

if __name__ == "__main__":
    qtherm = QThermSimModel()
    simulation_output = qtherm.run_simulation_pipeline()
    
    for idx, res in enumerate(simulation_output, 1):
        print(f"\n[Test Case {idx}]")
        print(f"  - Lattice Spacing: {res['lattice_spacing_nm']} nm")
        print(f"  - Phonon Resonance: {res['frequency_thz']} THz")
        print(f"  - Emitted Wavelength: {res['wavelength_um']} um")
        print(f"  - Evaluation: {res['evaluation']}")
