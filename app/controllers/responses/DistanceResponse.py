class DistanceResponse:
    
    @staticmethod
    def serialize(distance):
        return {
            'distance': distance
        }