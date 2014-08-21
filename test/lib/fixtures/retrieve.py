class MockRetrieveResponse:
    def __init__(self):
        self.id = '12345'
        self.fileProperties = []
        self.zipFile = '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AAAAAAAAAAAAAAAAdwAAAHVucGFja2FnZWQvY29tcG9uZW50cy9NeUNvbXBvbmVudE5hbWUuY29tcG9uZW50LW1ldGEueG1sUEsBAhQAFAAICAgA1okVRXVbhYFQBwAAsiIAADMAAAAAAAAAAAAAAAAAbAEAAHVucGFja2FnZWQvY29tcG9uZW50cy9NdWx0aXNlbGVjdFBpY2tsaXN0LmNvbXBvbmVudFBLAQIUABQACAgIANaJFUWpCW21lQAAAMEAAAA8AAAAAAAAAAAAAAAAAB0JAAB1bnBhY2thZ2VkL2NvbXBvbmVudHMvTXVsdGlzZWxlY3RQaWNrbGlzdC5jb21wb25lbnQtbWV0YS54bWxQSwECFAAUAAgICADWiRVF+E/WhhoAAAAkAAAAMAAAAAAAAAAAAAAAAAAcCgAAdW5wYWNrYWdlZC9jb21wb25lbnRzL015Q29tcG9uZW50TmFtZTIuY29tcG9uZW50UEsBAhQAFAAICAgA1okVRY4N+1OPAAAAvgAAADkAAAAAAAAAAAAAAAAAlAoAAHVucGFja2FnZWQvY29tcG9uZW50cy9NeUNvbXBvbmVudE5hbWUyLmNvbXBvbmVudC1tZXRhLnhtbFBLAQIUABQACAgIANaJFUX4T9aGGgAAACQAAABBAAAAAAAAAAAAAAAAAIoLAAB1bnBhY2thZ2VkL2NvbXBvbmVudHMvTXlWaXN1YWxmb3JjZUNvbXBvbmVudGpmZGtsZHNmbGtqLmNvbXBvbmVudFBLAQIUABQACAgIANaJFUXwe3EVmwAAAM8AAABKAAAAAAAAAAAAAAAAABMMAAB1bnBhY2thZ2VkL2NvbXBvbmVudHMvTXlWaXN1YWxmb3JjZUNvbXBvbmVudGpmZGtsZHNmbGtqLmNvbXBvbmVudC1tZXRhLnhtbFBLAQIUABQACAgIANaJFUX4T9aGGgAAACQAAAA2AAAAAAAAAAAAAAAAACYNAAB1bnBhY2thZ2VkL2NvbXBvbmVudHMvTXlWaXN1YWxmb3JjZUNvbXBvbmVudC5jb21wb25lbnRQSwECFAAUAAgICADWiRVF9NbsppAAAADEAAAAPwAAAAAAAAAAAAAAAACkDQAAdW5wYWNrYWdlZC9jb21wb25lbnRzL015VmlzdWFsZm9yY2VDb21wb25lbnQuY29tcG9uZW50LW1ldGEueG1sUEsBAhQAFAAICAgA1okVRQIG662KBAAAJwkAACMAAAAAAAAAAAAAAAAAoQ4AAHVucGFja2FnZWQvY29tcG9uZW50cy96aXAuY29tcG9uZW50UEsBAhQAFAAICAgA1okVRUFdZeeKAAAAsQAAACwAAAAAAAAAAAAAAAAAfBMAAHVucGFja2FnZWQvY29tcG9uZW50cy96aXAuY29tcG9uZW50LW1ldGEueG1sUEsBAhQAFAAICAgA1okVRfhP1oYaAAAAJAAAADAAAAAAAAAAAAAAAAAAYBQAAHVucGFja2FnZWQvY29tcG9uZW50cy9NeUNvbXBvbmVudE5hbWUxLmNvbXBvbmVudFBLAQIUABQACAgIANaJFUVNIG/gjwAAAL4AAAA5AAAAAAAAAAAAAAAAANgUAAB1bnBhY2thZ2VkL2NvbXBvbmVudHMvTXlDb21wb25lbnROYW1lMS5jb21wb25lbnQtbWV0YS54bWxQSwECFAAUAAgICADWiRVFZ5NfpbEDAABdBwAAKAAAAAAAAAAAAAAAAADOFQAAdW5wYWNrYWdlZC9jb21wb25lbnRzL3ppcEVudHJ5LmNvbXBvbmVudFBLAQIUABQACAgIANaJFUWvNVywjgAAALcAAAAxAAAAAAAAAAAAAAAAANUZAAB1bnBhY2thZ2VkL2NvbXBvbmVudHMvemlwRW50cnkuY29tcG9uZW50LW1ldGEueG1sUEsBAhQAFAAICAgA1okVReMCuMyfAAAA4QAAABYAAAAAAAAAAAAAAAAAwhoAAHVucGFja2FnZWQvcGFja2FnZS54bWxQSwUGAAAAABEAEQB0BgAApRsAAAAA'
