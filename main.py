import random
import time

class Microservice:
    def __init__(self, name, initial_stability=80):
        self.name = name
        # Stability (0-100): 100 is perfectly stable, 0 is highly unstable.
        # Lower stability means higher internal disorder, contributing to system entropy.
        self.stability = initial_stability

    def perform_task(self):
        # Simulate an internal operation. Small chance of a minor issue reducing stability.
        if random.random() < 0.15: # 15% chance of a minor issue
            self.stability = max(0, self.stability - random.randint(1, 3))
            # print(f"  [{self.name}] Minor issue. Stability: {self.stability}")
        return self.stability

    def improve_stability(self, amount):
        # Simulate internal improvements or fixes
        self.stability = min(100, self.stability + amount)

    def __repr__(self):
        return f"Service({self.name}, Stability: {self.stability})"

class MicroserviceEcosystem:
    def __init__(self, service_names, initial_system_entropy=20):
        self.services = {name: Microservice(name) for name in service_names}
        # System entropy (0-100): A measure of overall disorder and unpredictability.
        # Higher values mean more chaos, lower values mean more order/stability.
        self.system_entropy = initial_system_entropy
        print(f"Ecosystem initialized with {len(self.services)} services.")
        print(f"Initial System Entropy: {self.system_entropy:.2f}")

    def _get_average_instability(self):
        # Average (100 - stability) for all services
        return sum(100 - s.stability for s in self.services.values()) / len(self.services)

    def simulate_interaction(self):
        # Pick two random services to interact
        if len(self.services) < 2:
            return

        s1_name, s2_name = random.sample(list(self.services.keys()), 2)
        s1 = self.services[s1_name]
        s2 = self.services[s2_name]

        s1.perform_task() # Each service performs its part, potentially reducing its stability
        s2.perform_task()

        # Entropy naturally increases with interactions, especially if services are unstable.
        # This models the increased complexity, communication overhead, and potential for failures
        # that arise from interactions in a distributed system.
        interaction_base_entropy_gain = random.uniform(0.5, 1.5)
        # Instability of interacting services amplifies entropy gain
        instability_factor = (100 - s1.stability + 100 - s2.stability) / 200 # 0 to 1
        entropy_gain = interaction_base_entropy_gain * (1 + instability_factor * 2) # Amplified if services are unstable

        self.system_entropy += entropy_gain
        self.system_entropy = min(100, self.system_entropy) # Cap entropy at 100

        print(f"  Interaction between {s1.name} and {s2.name}. Entropy increased by {entropy_gain:.2f}.")

    def apply_governance_and_monitoring(self, effort_level=1.0):
        # This simulates "work" done to reduce system entropy.
        # Examples: refactoring, improving documentation, implementing better observability,
        # standardizing communication protocols, fixing bugs, etc.
        # This is analogous to doing work on a physical system to reduce its entropy and maintain order.
        entropy_reduction = random.uniform(2.0, 5.0) * effort_level
        self.system_entropy = max(0, self.system_entropy - entropy_reduction)

        # Governance also helps improve individual service stabilities
        for service in self.services.values():
            service.improve_stability(random.randint(1, 4))

        print(f"--- Governance/Monitoring applied. System Entropy reduced by {entropy_reduction:.2f} ---")

    def get_status(self):
        avg_stability = sum(s.stability for s in self.services.values()) / len(self.services)
        return {
            "system_entropy": self.system_entropy,
            "average_service_stability": avg_stability,
            "services_status": {s.name: s.stability for s in self.services.values()}
        }

# --- Simulation ---
if __name__ == "__main__":
    service_names = ["AuthService", "UserService", "ProductService", "OrderService", "PaymentService"]
    ecosystem = MicroserviceEcosystem(service_names)

    print("\n--- Simulating Microservice Ecosystem Evolution ---")
    print("This simulation models a microservice system using thermodynamic concepts:")
    print(" - System Entropy: Overall disorder/complexity. Tends to increase with interactions.")
    print(" - Service Stability: Internal health of a microservice. Affects entropy increase.")
    print(" - Governance/Monitoring: 'Work' applied to reduce entropy and improve stability.")
    print("Goal: Observe how consistent 'work' is needed to prevent entropy from spiraling out of control.")

    simulation_steps = 25
    for i in range(simulation_steps):
        print(f"\n--- Step {i+1} ---")

        # Simulate interactions (natural tendency towards increased entropy)
        num_interactions = random.randint(1, 4)
        for _ in range(num_interactions):
            ecosystem.simulate_interaction()

        # Periodically apply governance/monitoring (effort to reduce entropy)
        if (i + 1) % 5 == 0: # Every 5 steps, apply governance
            ecosystem.apply_governance_and_monitoring(effort_level=1.5) # Higher effort
            print(f"  (Applied higher effort governance due to accumulated complexity)")
        elif (i + 1) % 2 == 0: # Every other step, apply standard governance
            ecosystem.apply_governance_and_monitoring(effort_level=0.7) # Standard effort

        status = ecosystem.get_status()
        print(f"Current System Entropy: {status['system_entropy']:.2f}")
        print(f"Average Service Stability: {status['average_service_stability']:.2f}")
        # print(f"Service Stabilities: {status['services_status']}")
        time.sleep(0.7) # Pause for readability

    print("\n--- Simulation End ---")
    final_status = ecosystem.get_status()
    print(f"Final System Entropy: {final_status['system_entropy']:.2f}")
    print(f"Final Average Service Stability: {final_status['average_service_stability']:.2f}")
    print("\nObservation:")
    print("Without continuous 'work' (governance, monitoring), system entropy would tend to increase,")
    print("leading to a more chaotic, unpredictable, and harder-to-manage microservice ecosystem.")
    print("This illustrates the constant effort needed to maintain order in distributed systems.")
