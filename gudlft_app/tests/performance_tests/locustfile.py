from locust import HttpUser, task, between


class ProjectPerfTest(HttpUser):
    """
    Class defining tasks to simulate.
    """
    wait_time = between(1, 3)

    @task
    def index(self):
        self.client.get("/")

    @task()
    def show_summary(self):
        self.client.post("/show-summary", data={'email': 'john@simplylift.co'})

    @task()
    def book(self):
        competition_name = "Summer Festival"
        club_name = "Simply Lift"
        self.client.get(f"/book/{competition_name}/{club_name}")

    @task()
    def purchase_places(self):
        competition_name = "Summer Festival"
        club_name = "Simply Lift"
        places_required = "5"
        self.client.post(
            "/purchase-places",
            data={"places": places_required, "club": club_name, "competition": competition_name}
        )

    @task()
    def display_board(self):
        self.client.get("/display-board")

    @task()
    def logout(self):
        self.client.get("/logout")