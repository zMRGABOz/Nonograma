import pygame

class Context:
    _state = None
    
    def __init__(self, state: 'State') -> None:
        self.transition_to(state)
        
    def transition_to(self, state: 'State'):
        self._state = state
        self._state.context = self

    def request1(self):
        self._state.go_to()

    def request2(self):
        self._state.back_to()

    def run(self):
        running = True
        screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("Nonograma")

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                self._state.handle_events(event)

            self._state.draw(screen)
            pygame.display.flip()
        pygame.quit()