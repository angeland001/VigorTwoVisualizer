using System.Collections;
using System.Collections.Generic;
using System;
using UnityEngine;

public class SMPL_Controller : MonoBehaviour
{
    Vector3[,] joint_motions;
    int frame_counter = 0;
    // Start is called before the first frame update
    void Start()
    {
        Debug.Log("a");
        string fileData = System.IO.File.ReadAllText("Assets/Data/out.csv");
        string[] lines = fileData.Split("\n");
        joint_motions = new Vector3[lines.Length, lines[0].Split(",").Length / 3];

        for (int i = 0; i < lines.Length; i++){
            string[] frame_joints = lines[i].Split(",");
            for (int j = 0; j < frame_joints.Length; j += 3){
                Vector3 joint = new Vector3(float.Parse(frame_joints[j]), float.Parse(frame_joints[j + 1]), float.Parse(frame_joints[j + 2]));
                joint_motions[i, j / 3] = joint;
            }
        }

    }
    
    // Update is called once per frame
    void Update()
    {
        foreach (Transform t in gameObject.GetComponentsInChildren<Transform>()){
            if (t.name == "lowerleg_r"){
                t.rotation = Quaternion.AngleAxis(270, joint_motions[frame_counter, 5]);
            }
        }

        if (frame_counter < joint_motions.GetLength(0) - 1){
            frame_counter += 1;
        } else {
            frame_counter = 0;
        }
    }
}
