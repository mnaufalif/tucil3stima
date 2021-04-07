from prio_queue import PriorityQueue
from node import Node
from graph import Graph
from helper import distance
def a_star():
    expanded_nodes_id = [] # untuk tracking node mana saja yang sudah diekspan

    Node.set_start_end_handler()

    # _variables containing reference to the real object_
    start_node = Node.get_start_node()
    end_node = Node.get_end_node()
    adj_matrix = Graph.adjmatrix
    
    # set prev_distance start_node menjadi 0
    start_node.update_prev_distance(0)

    # buat PriorityQueue baru (pq)
    pq = PriorityQueue()

    #[status] start_node seakan-akan masuk pq
    #-- current_node adalah node yang akan diekspan
    current_node = start_node
    #[status] start_node seakan-akan keluar pq (diekspan)
    
    # helper boolean
    route_exist = True
    all_neighbour_checked = False
    while(current_node.id != end_node.id and not (all_neighbour_checked)):
        # idx untuk mencari node tetangga
        idx = current_node.get_index()
        neighbour = adj_matrix[idx]
        no_neighbour_left = True
        for i in range(len(neighbour)):
            if (neighbour[i]!='0' and (i+1) not in expanded_nodes_id): # jika tetangga dan belum pernah diekspan
                no_neighbour_left = False
                # TODO: simpan dulu prev_node, prev_distance, dan end_distance ke variabel lokal ds, pn, de (distance_start, previous_node, distance_end).
                # jika checked_node belum di pq (prev_distance = INFINITY_R), update prev_distance dan prev_node, lalu tambahkan checked_node ke pq
                # jika sudah di pq dan nilai ds < prev_distance  

                #-- di sini, current_node = prev_node dari checked_node
                #-- nantinya, checked_node akan dimasukkan ke pq (PriorityQueue)

                checked_node = Node.get_node(i+1) # simpan neighbour[i] ke checked_node
                
                # menyimpan ke variabel lokal
                ds = distance(current_node.lat, current_node.lng, checked_node.lat, checked_node.lng) + current_node.prev_distance
                pn = current_node
                de = Node.list_distance[checked_node.id-1]

                #-- setelah itu, priority_weight checked_node perlu dihitung
                #-- priority_weight = prev_distance dari checked_node + jarak dari checked_node ke end_node
                priority_weight = ds + de

                # cek apakah checked_node ada di pq
                exist = pq.check_value(checked_node)

                if not exist:
                    # update prev_distance
                    checked_node.update_prev_distance(ds)
                    # update prev_node
                    checked_node.update_prev_node(pn)

                    pq.put((priority_weight, checked_node))
                else:
                    # jika ds < prev_distance, update checked_node pada pq
                    if ds < checked_node.prev_distance:
                        # hapus node lama
                        key = checked_node.prev_distance + de
                        pq.del_by_key(key)

                        # update prev_distance
                        checked_node.update_prev_distance(ds)
                        # update prev_node
                        checked_node.update_prev_node(pn)

                        pq.put((priority_weight, checked_node))


        #-- setelah for loop dilakukan, id current_node akan dicatat di expanded_nodes_id
        #-- setelah itu, elemen terdepan dari pq akan diekspan (diset menjadi current_node)
        expanded_nodes_id.append(current_node.id)
        if no_neighbour_left and len(pq.pq) == 0:
            all_neighbour_checked = True
        else:
            current_node = pq.get()[1]
    
    if (current_node.id!=end_node.id and (all_neighbour_checked and len(pq.pq)==0)):
        route_exist = False

    print("Expanded Node:", end=" ")
    print(expanded_nodes_id, end = "")
    if route_exist:
        print(" -> %d [FOUND]"%(end_node.id))
    else:
        print(" -> X [NOT FOUND]")

    if not route_exist:
        print("Tidak ada rute yang menghubungkan kedua titik.")
        return []
    
    path = []
    while(current_node.prev_node != None):
        path.insert(0, current_node)
        current_node = current_node.prev_node
    path.insert(0, current_node)

    jarak_total = 0
    print()
    for i in range(len(path)):
        prev_distance = 0
        if i!=0:
            prev_distance = path[i-1].prev_distance
        jarak = path[i].prev_distance - prev_distance
        print(path[i].id, '-', path[i].name, "[%f km]"%(jarak))
        jarak_total += jarak
    
    print()
    print("Jarak total: %f km"%(jarak_total))
    print("Path:", end = " ")
    for i in range(len(path)):
        print("[%d] %s"%(path[i].id,path[i].name), end="")
        if i < len(path)-1:
            print(" -> ", end="")
    return path
