import os.path, sys
sys.path.append(os.path.join('/'.join(os.path.dirname(os.path.realpath(__file__)).split('/')[:-1])))
import backend.backend as be


class Context_PathUuid_TelinkLocalidImpl:

    @classmethod
    def get(cls, uuid, localId):
        print 'handling get'
        if uuid in be.Context._path:
            if localId in be.Context._path[uuid]._telink:
                return be.Context._path[uuid]._telink[localId]
            else:
                raise KeyError('localId')
        else:
            raise KeyError('uuid')
