import cloudant
from cloudant.client import CouchDB

ROW_LIMIT = 200


class QueryClient:
    def __init__(self):
        self.server_url = 'https://mikerhodes.cloudant.com'
        self.ddoc_id = '_design/view1'
        self.index_name = 'geo'
        self.db_name = 'airportdb'

    def airports_inside(self, bounding_boxes):
        """
        Retrieves within the airports the given bounding boxes

        :param list bounding_boxes: boxes where airports are searched
        :returns: List of airports
        """
        airports = []
        try:
            client = CouchDB(None, None, url=self.server_url, admin_party=True, connect=True)
            db = cloudant.database.CloudantDatabase(client, self.db_name, ROW_LIMIT)
            for bounding_box in bounding_boxes:
                query = self.create_query_string(bounding_box)
                optional_args = dict(query=query, include_docs=True, limit=ROW_LIMIT)
                is_query_finished = False
                while not is_query_finished:
                    resp = db.get_search_result(self.ddoc_id, self.index_name, **optional_args)
                    airports += resp["rows"]
                    optional_args.update({'bookmark': resp['bookmark']})
                    if 0 == len(resp['rows']):
                        is_query_finished = True
        finally:
            client.disconnect()
        return airports

    def create_query_string(self, bounding_box):
        query = 'lon:[' + str(bounding_box.longitude_min) + ' TO ' + str(
            bounding_box.longitude_max) + '] AND lat:[' + str(
            bounding_box.latitude_min) + ' TO ' + str(bounding_box.latitude_max) + ']'
        return query
